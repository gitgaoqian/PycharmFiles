# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CloudROS.ui'
#
# Created: Wed May 16 20:57:10 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from threading import Thread
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
        Form.resize(635, 507)
        self.LabelTitle = QtGui.QLabel(Form)
        self.LabelTitle.setGeometry(QtCore.QRect(180, 40, 331, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Droid Sans Fallback"))
        font.setPointSize(20)
        self.LabelTitle.setFont(font)
        self.LabelTitle.setObjectName(_fromUtf8("LabelTitle"))
        self.LabelServiceType = QtGui.QLabel(Form)
        self.LabelServiceType.setGeometry(QtCore.QRect(100, 130, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelServiceType.setFont(font)
        self.LabelServiceType.setObjectName(_fromUtf8("LabelServiceType"))
        self.ComboBoxType = QtGui.QComboBox(Form)
        self.ComboBoxType.setGeometry(QtCore.QRect(190, 140, 78, 27))
        self.ComboBoxType.setObjectName(_fromUtf8("ComboBoxType"))
        self.ComboBoxType.addItem(_fromUtf8(""))
        self.ComboBoxType.addItem(_fromUtf8(""))
        self.LabelComputeName = QtGui.QLabel(Form)
        self.LabelComputeName.setGeometry(QtCore.QRect(100, 310, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelComputeName.setFont(font)
        self.LabelComputeName.setObjectName(_fromUtf8("LabelComputeName"))
        self.ComboBoxComputeName = QtGui.QComboBox(Form)
        self.ComboBoxComputeName.setGeometry(QtCore.QRect(190, 310, 71, 27))
        self.ComboBoxComputeName.setObjectName(_fromUtf8("ComboBoxComputeName"))
        self.ComboBoxComputeName.addItem(_fromUtf8(""))
        self.ComboBoxComputeName.addItem(_fromUtf8(""))
        self.ComboBoxComputeName.addItem(_fromUtf8(""))
        self.LabelServiceType_2 = QtGui.QLabel(Form)
        self.LabelServiceType_2.setGeometry(QtCore.QRect(70, 260, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LabelServiceType_2.setFont(font)
        self.LabelServiceType_2.setObjectName(_fromUtf8("LabelServiceType_2"))
        self.LabelServiceType_3 = QtGui.QLabel(Form)
        self.LabelServiceType_3.setGeometry(QtCore.QRect(340, 260, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LabelServiceType_3.setFont(font)
        self.LabelServiceType_3.setObjectName(_fromUtf8("LabelServiceType_3"))
        self.ComboBoxComputeAction = QtGui.QComboBox(Form)
        self.ComboBoxComputeAction.setGeometry(QtCore.QRect(190, 360, 71, 27))
        self.ComboBoxComputeAction.setObjectName(_fromUtf8("ComboBoxComputeAction"))
        self.ComboBoxComputeAction.addItem(_fromUtf8(""))
        self.ComboBoxComputeAction.addItem(_fromUtf8(""))
        self.LabelComputeAction = QtGui.QLabel(Form)
        self.LabelComputeAction.setGeometry(QtCore.QRect(100, 360, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelComputeAction.setFont(font)
        self.LabelComputeAction.setObjectName(_fromUtf8("LabelComputeAction"))
        self.ComboBoxStoreID = QtGui.QComboBox(Form)
        self.ComboBoxStoreID.setGeometry(QtCore.QRect(470, 310, 71, 27))
        self.ComboBoxStoreID.setObjectName(_fromUtf8("ComboBoxStoreID"))
        self.ComboBoxStoreID.addItem(_fromUtf8(""))
        self.ComboBoxStoreID.addItem(_fromUtf8(""))
        self.ComboBoxStoreID.addItem(_fromUtf8(""))
        self.ComboBoxStoreID.addItem(_fromUtf8(""))
        self.ComboBoxStoreID.addItem(_fromUtf8(""))
        self.ComboBoxStoreID.addItem(_fromUtf8(""))
        self.LabelStoreID = QtGui.QLabel(Form)
        self.LabelStoreID.setGeometry(QtCore.QRect(380, 310, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelStoreID.setFont(font)
        self.LabelStoreID.setObjectName(_fromUtf8("LabelStoreID"))
        self.LabelStoreAction = QtGui.QLabel(Form)
        self.LabelStoreAction.setGeometry(QtCore.QRect(380, 360, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelStoreAction.setFont(font)
        self.LabelStoreAction.setObjectName(_fromUtf8("LabelStoreAction"))
        self.ComboBoxStoreAction = QtGui.QComboBox(Form)
        self.ComboBoxStoreAction.setGeometry(QtCore.QRect(470, 360, 71, 27))
        self.ComboBoxStoreAction.setObjectName(_fromUtf8("ComboBoxStoreAction"))
        self.ComboBoxStoreAction.addItem(_fromUtf8(""))
        self.ComboBoxStoreAction.addItem(_fromUtf8(""))
        self.ButtonRequest = QtGui.QPushButton(Form)
        self.ButtonRequest.setGeometry(QtCore.QRect(260, 400, 111, 51))
        self.ButtonRequest.setObjectName(_fromUtf8("ButtonRequest"))
        self.lineEditCloudServer = QtGui.QLineEdit(Form)
        self.lineEditCloudServer.setGeometry(QtCore.QRect(420, 140, 113, 27))
        self.lineEditCloudServer.setText(_fromUtf8(""))
        self.lineEditCloudServer.setObjectName(_fromUtf8("lineEditCloudServer"))
        self.LabelCloudServer = QtGui.QLabel(Form)
        self.LabelCloudServer.setGeometry(QtCore.QRect(340, 130, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.LabelCloudServer.setFont(font)
        self.LabelCloudServer.setObjectName(_fromUtf8("LabelCloudServer"))
        self.LabelRequestConfig = QtGui.QLabel(Form)
        self.LabelRequestConfig.setGeometry(QtCore.QRect(40, 220, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LabelRequestConfig.setFont(font)
        self.LabelRequestConfig.setObjectName(_fromUtf8("LabelRequestConfig"))
        self.LabelPreConfig = QtGui.QLabel(Form)
        self.LabelPreConfig.setGeometry(QtCore.QRect(50, 100, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.LabelPreConfig.setFont(font)
        self.LabelPreConfig.setObjectName(_fromUtf8("LabelPreConfig"))
        self.ButtonBridge = QtGui.QPushButton(Form)
        self.ButtonBridge.setGeometry(QtCore.QRect(260, 180, 111, 51))
        self.ButtonBridge.setObjectName(_fromUtf8("ButtonBridge"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.LabelTitle.setText(_translate("Form", "CloudROS云服务管理界面", None))
        self.LabelServiceType.setText(_translate("Form", "服务类型", None))
        self.ComboBoxType.setItemText(0, _translate("Form", "compute", None))
        self.ComboBoxType.setItemText(1, _translate("Form", "storage", None))
        self.LabelComputeName.setText(_translate("Form", "服务名称", None))
        self.ComboBoxComputeName.setItemText(0, _translate("Form", "stereo_proc", None))
        self.ComboBoxComputeName.setItemText(1, _translate("Form", "addition", None))
        self.ComboBoxComputeName.setItemText(2, _translate("Form", "teleop", None))
        self.LabelServiceType_2.setText(_translate("Form", "计算服务", None))
        self.LabelServiceType_3.setText(_translate("Form", "存储服务", None))
        self.ComboBoxComputeAction.setItemText(0, _translate("Form", "start", None))
        self.ComboBoxComputeAction.setItemText(1, _translate("Form", "stop", None))
        self.LabelComputeAction.setText(_translate("Form", "服务动作", None))
        self.ComboBoxStoreID.setItemText(0, _translate("Form", "1", None))
        self.ComboBoxStoreID.setItemText(1, _translate("Form", "2", None))
        self.ComboBoxStoreID.setItemText(2, _translate("Form", "3", None))
        self.ComboBoxStoreID.setItemText(3, _translate("Form", "4", None))
        self.ComboBoxStoreID.setItemText(4, _translate("Form", "5", None))
        self.ComboBoxStoreID.setItemText(5, _translate("Form", "6", None))
        self.LabelStoreID.setText(_translate("Form", "机器人ID", None))
        self.LabelStoreAction.setText(_translate("Form", "服务动作", None))
        self.ComboBoxStoreAction.setItemText(0, _translate("Form", "store", None))
        self.ComboBoxStoreAction.setItemText(1, _translate("Form", "fetch", None))
        self.ButtonRequest.setText(_translate("Form", "服务请求", None))
        self.LabelCloudServer.setText(_translate("Form", "云服务器", None))
        self.LabelRequestConfig.setText(_translate("Form", "请求服务配置", None))
        self.LabelPreConfig.setText(_translate("Form", "预配置", None))
        self.ButtonBridge.setText(_translate("Form", "桥梁节点", None))
class CloudROSDisplay(QtGui.QWidget,Ui_Form):    
    def __init__(self):    
        super(CloudROSDisplay,self).__init__()    
        self.setupUi(self)  #(self)这里理解为传入的参数是类mywindow的实例
        #槽函数链接两种不同形式e
        self.ButtonBridge.clicked.connect(self.StartBridge)
        self.connect(self.ButtonRequest,QtCore.SIGNAL("clicked()"),self.StartRequest)
    def StartBridge(self):
        Thread_bridge = Thread(target=self.run_bridge, args=())
        Thread_bridge.start()
    def run_bridge(self):
        Interface = self.lineEditCloudServer.text()
        service_type = self.ComboBoxType.currentText()
        if service_type == "compute":
            os.system("rosrun cloud_v2 bridge.py")
        if service_type == "storage":
            os.system("rosrun neu_wgg bridge3.py")
    def StartRequest(self):
        service_type = self.ComboBoxType.currentText()
        if service_type == "compute":
            compute_name = unicode(self.ComboBoxComputeName.currentText())
            compute_action = unicode(self.ComboBoxComputeAction.currentText())
            os.system("rosrun cloud_v2 client.py "+compute_name+" "+compute_action)
        if service_type == "storage":
            robotID = unicode(self.ComboBoxStoreID.currentText())
            store_action = unicode(self.ComboBoxStoreAction.currentText())
            os.system("rosrun neu_wgg client3.py "+robotID+" "+store_action)
if __name__=="__main__":  
    import sys  
    app=QtGui.QApplication(sys.argv)  
    myshow=CloudROSDisplay()  
    myshow.show()   
    sys.exit(app.exec_()) 

