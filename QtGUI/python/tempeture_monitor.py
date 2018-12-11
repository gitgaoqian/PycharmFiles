# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tempeture_monitor.ui'
#
# Created: Mon Nov  6 21:30:34 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.lcdTemp = QtGui.QLCDNumber(Form)
        self.lcdTemp.setGeometry(QtCore.QRect(120, 70, 151, 61))
        self.lcdTemp.setObjectName(_fromUtf8("lcdTemp"))
        self.labelTemp = QtGui.QLabel(Form)
        self.labelTemp.setGeometry(QtCore.QRect(100, 50, 101, 16))
        self.labelTemp.setObjectName(_fromUtf8("labelTemp"))
        self.labelAlarm = QtGui.QLabel(Form)
        self.labelAlarm.setGeometry(QtCore.QRect(90, 140, 111, 16))
        self.labelAlarm.setObjectName(_fromUtf8("labelAlarm"))
        self.sliderAlarm = QtGui.QSlider(Form)
        self.sliderAlarm.setGeometry(QtCore.QRect(120, 160, 160, 16))
        self.sliderAlarm.setProperty("value", 30)
        self.sliderAlarm.setOrientation(QtCore.Qt.Horizontal)
        self.sliderAlarm.setObjectName(_fromUtf8("sliderAlarm"))
        
          #Add timer
        self.timerTemp = QtCore.QTimer()       
     
       
        # Add slots
        self.sliderAlarm.valueChanged.connect(self.sliderAlarm_ValueChanged)
        self.timerTemp.timeout.connect(self.timerTemp_TimeOut)
        # Use the timeout event to initialize the LCD
        self.timerTemp_TimeOut()
        # Start timer, time out per 2 seconds
        self.timerTemp.start(2000)
       
       


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.labelTemp.setText(_translate("Form", "cpu tempeture", None))
        self.labelAlarm.setText(_translate("Form", "alarm tempeture", None))
        
       # Event triggered when the value of labelAlarm changed
    def sliderAlarm_ValueChanged(self):
        self.labelAlarm.setText("Alarm: " + str(self.sliderAlarm.value()) + "C")
       
    # Event triggered when timerTemp time out
    def timerTemp_TimeOut(self):
        # Get temperature from sensor file
        sensor = os.popen("cat /sys/class/thermal/thermal_zone0/temp")
        temp = float(sensor.readline()) / 1000
        alarm = float(self.sliderAlarm.value())
        # Display temperature
        self.lcdTemp.display("%.1fC" % temp)
        # Check whether the temperature is too high
        if temp <= alarm * 0.6:
            self.lcdTemp.setStyleSheet("color: green")
        elif temp <= alarm * 0.8:
            self.lcdTemp.setStyleSheet("color: orange")
        elif temp <= alarm:
            self.lcdTemp.setStyleSheet("color: red")
        else:
            self.lcdTemp.setStyleSheet("color: red")
            msg = QtGui.QMessageBox()
            msg.setWindowTitle("Alarm")
            msg.setText("Temperature is too high!")
            msg.setIcon(QtGui.QMessageBox.Warning)
            msg.exec_()
            # You can do something else here, like shut down the system


if __name__=="__main__":  
    import sys  
    app=QtGui.QApplication(sys.argv)  
    widget=QtGui.QWidget()  
    ui=Ui_Form()  
    ui.setupUi(widget)  
    widget.show()  
    sys.exit(app.exec_())  
    