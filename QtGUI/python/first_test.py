# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firsttest.ui'
#
# Created: Mon Nov  6 10:45:44 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_test(object):
    def setupUi(self, test):
        test.setObjectName(_fromUtf8("test"))
        test.resize(400, 300)
        self.qiutButton = QtGui.QPushButton(test)
        self.qiutButton.setGeometry(QtCore.QRect(300, 220, 80, 23))
        self.qiutButton.setObjectName(_fromUtf8("qiutButton"))

        self.retranslateUi(test)
        QtCore.QMetaObject.connectSlotsByName(test)
      

    def retranslateUi(self, test):
        test.setWindowTitle(_translate("test", "Form", None))
        self.qiutButton.setText(_translate("test", "quitButton", None))
class mywindow(QtGui.QWidget,Ui_test):    
    def __init__(self):    
        super(mywindow,self).__init__()    
        self.setupUi(self)  #(self)这里理解为传入的参数是类mywindow的实例
        #信号与槽的多种格式:
        QtCore.QObject.connect(self.qiutButton,QtCore.SIGNAL("clicked()"),self.myPrint)
        #self.qiutButton.clicked.connect(self.myPrint)   #槽函数不用加括号
    def myPrint(self):                                #定义槽  
        print("helloWorld")  

if __name__=="__main__":  
    import sys  
    app=QtGui.QApplication(sys.argv)  
    myshow=mywindow()  
    myshow.show()   
    sys.exit(app.exec_()) 
