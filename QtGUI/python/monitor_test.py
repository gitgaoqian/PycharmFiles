# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitor_test.ui'
#
# Created: Fri Nov 10 10:28:36 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import rospy
import os
import thread
from std_msgs.msg import Float64
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
        self.display_label = QtGui.QLabel(Form)
        self.display_label.setGeometry(QtCore.QRect(80, 90, 59, 15))
        self.display_label.setObjectName(_fromUtf8("display_label"))
        self.display_Button = QtGui.QPushButton(Form)
        self.display_Button.setGeometry(QtCore.QRect(230, 90, 51, 23))
        self.display_Button.setObjectName(_fromUtf8("display_Button"))
        self.display_text = QtGui.QLineEdit(Form)
        self.display_text.setGeometry(QtCore.QRect(110, 90, 113, 23))
        self.display_text.setObjectName(_fromUtf8("display_text"))
        self.plot_Button = QtGui.QPushButton(Form)
        self.plot_Button.setGeometry(QtCore.QRect(290, 90, 51, 23))
        self.plot_Button.setObjectName(_fromUtf8("plot_Button"))
         #信号与槽函数连接
        self.display_Button.clicked.connect(self.display)
        self.plot_Button.clicked.connect(self.plot)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.display_label.setText(_translate("Form", "信息", None))
        self.display_Button.setText(_translate("Form", "显示", None))
        self.plot_Button.setText(_translate("Form", "绘图", None))

    def callback(self,data):
        value = str(data.data)
        self.display_text.setText(value)
    def display(self):                                #定义槽  
        rospy.Subscriber('Data',Float64,self.callback)
    def plot_fun(self):
        os.system('rosrun rqt_plot rqt_plot')  
    def plot(self):
        thread.start_new_thread(self.plot_fun,())
        
if __name__=="__main__":  
    import sys  
    rospy.init_node('monitor',anonymous = True)
    app=QtGui.QApplication(sys.argv)  #每个 Qt 应用程序都必须有且只有一个 QApplication 对象,
#采用 sys.argv 作为参数,便于程序处理命令行参数。
    widget=QtGui.QWidget()  #创建一个组件对象
    ui=Ui_Form()  
    ui.setupUi(widget)  #类实例化，组件对象中放置元件
    widget.show()  
    sys.exit(app.exec_()) 

