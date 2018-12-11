# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'step_motor.ui'
#
# Created: Wed Jan  3 20:24:12 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
import serial
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
        Form.resize(370, 327)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        Form.setFont(font)
        self.label_title = QtGui.QLabel(Form)
        self.label_title.setGeometry(QtCore.QRect(100, 10, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_title.setFont(font)
        self.label_title.setObjectName(_fromUtf8("label_title"))
        self.label_dir = QtGui.QLabel(Form)
        self.label_dir.setGeometry(QtCore.QRect(50, 170, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_dir.setFont(font)
        self.label_dir.setObjectName(_fromUtf8("label_dir"))
        self.Button_pos = QtGui.QPushButton(Form)
        self.Button_pos.setGeometry(QtCore.QRect(130, 160, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Button_pos.setFont(font)
        self.Button_pos.setObjectName(_fromUtf8("Button_pos"))
        self.Button_rev = QtGui.QPushButton(Form)
        self.Button_rev.setGeometry(QtCore.QRect(240, 160, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Button_rev.setFont(font)
        self.Button_rev.setObjectName(_fromUtf8("Button_rev"))
        self.label_vel = QtGui.QLabel(Form)
        self.label_vel.setGeometry(QtCore.QRect(50, 250, 66, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_vel.setFont(font)
        self.label_vel.setObjectName(_fromUtf8("label_vel"))
        self.Slider_vel = QtGui.QSlider(Form)
        self.Slider_vel.setGeometry(QtCore.QRect(140, 250, 160, 29))
        self.Slider_vel.setMinimum(80)
        self.Slider_vel.setMaximum(120)
        self.Slider_vel.setSingleStep(5)
        self.Slider_vel.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_vel.setObjectName(_fromUtf8("Slider_vel"))
        self.Button_start = QtGui.QPushButton(Form)
        self.Button_start.setGeometry(QtCore.QRect(130, 80, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Button_start.setFont(font)
        self.Button_start.setObjectName(_fromUtf8("Button_start"))
        self.Button_stop = QtGui.QPushButton(Form)
        self.Button_stop.setGeometry(QtCore.QRect(240, 80, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.Button_stop.setFont(font)
        self.Button_stop.setObjectName(_fromUtf8("Button_stop"))
        self.label_enable = QtGui.QLabel(Form)
        self.label_enable.setGeometry(QtCore.QRect(50, 90, 71, 17))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_enable.setFont(font)
        self.label_enable.setObjectName(_fromUtf8("label_enable"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_title.setText(_translate("Form", "步进电机控制上位机", None))
        self.label_dir.setText(_translate("Form", "方向控制", None))
        self.Button_pos.setText(_translate("Form", "正向", None))
        self.Button_rev.setText(_translate("Form", "反向", None))
        self.label_vel.setText(_translate("Form", "脉宽调节", None))
        self.Button_start.setText(_translate("Form", "启动", None))
        self.Button_stop.setText(_translate("Form", "停止", None))
        self.label_enable.setText(_translate("Form", "使能开关", None))

class mywindow(QtGui.QWidget,Ui_Form):    
    def __init__(self):    
        super(mywindow,self).__init__()    
        self.setupUi(self)  #(self)这里理解为传入的参数是类mywindow的实例   
        self.ser=serial.Serial("/dev/ttyACM0",115200,timeout=10)
     #槽函数链接
        self.Button_start.clicked.connect(self.send_start_enable)
        self.Button_stop.clicked.connect(self.send_stop_enable)
        self.Button_pos.clicked.connect(self.send_posdir)
        self.Button_rev.clicked.connect(self.send_revdir)
        self.Slider_vel.valueChanged.connect(self.send_vel)
    def send_start_enable(self):
        self.ser.write("E0")
    def send_stop_enable(self):
        self.ser.write("E1")
    def send_posdir(self):
        self.ser.write("D1")
    def send_revdir(self):
        self.ser.write("D0")
    def send_vel(self):
        vel=self.Slider_vel.value()
        if vel < 10:
            send_vel='00'+str(vel)
        elif vel >= 10 and vel < 100:
            send_vel='0'+str(vel)
        elif vel >= 100 and vel <= 200:
            send_vel=str(vel)
        self.ser.write('V'+send_vel)
if __name__=="__main__":  
    app=QtGui.QApplication(sys.argv)  #每一个 PyQt4 程序都需要有一个 application 对象
    myshow=mywindow()  
    myshow.show()  
    sys.exit(app.exec_()) 
    #exec_()方法的作用是“进入程序的主循环,不用sys.exit(app.exec_())，只使用app.exec_()，程序一样可以正常运行，但是关闭窗口后主进程却不会退出,
    

