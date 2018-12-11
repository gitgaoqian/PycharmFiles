# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitor708.ui'
#
# Created: Mon Jul  9 08:36:32 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui
import rospy
from neu_wgg.msg import env_and_angle
import sys
pre_path = "/home/ros/pycharm/MyFiles/NEU_GDMAP/"
sys.path.append(pre_path+'neu_program')#把其他文件夹的py路径添加过来
import cv2
import sign
#环境信息
temp=0
hum=0
#地理位置信息
longitude=0
latitude=0
global exo_id

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
        Form.resize(489, 740)
        font = QtGui.QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.header = QtGui.QLabel(Form)
        self.header.setGeometry(QtCore.QRect(160, 40, 221, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.header.setFont(font)
        self.header.setObjectName(_fromUtf8("header"))
        self.label_env = QtGui.QLabel(Form)
        self.label_env.setGeometry(QtCore.QRect(30, 170, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_env.setFont(font)
        self.label_env.setObjectName(_fromUtf8("label_env"))
        self.lineEdit_tem = QtGui.QLineEdit(Form)
        self.lineEdit_tem.setGeometry(QtCore.QRect(150, 210, 71, 23))
        self.lineEdit_tem.setObjectName(_fromUtf8("lineEdit_tem"))
        self.lineEdit_hum = QtGui.QLineEdit(Form)
        self.lineEdit_hum.setGeometry(QtCore.QRect(330, 210, 71, 23))
        self.lineEdit_hum.setObjectName(_fromUtf8("lineEdit_hum"))
        self.label_hum = QtGui.QLabel(Form)
        self.label_hum.setGeometry(QtCore.QRect(250, 210, 81, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        font.setPointSize(12)
        self.label_hum.setFont(font)
        self.label_hum.setObjectName(_fromUtf8("label_hum"))
        self.label_long = QtGui.QLabel(Form)
        self.label_long.setGeometry(QtCore.QRect(50, 270, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        self.label_long.setFont(font)
        self.label_long.setObjectName(_fromUtf8("label_long"))
        self.label_tem = QtGui.QLabel(Form)
        self.label_tem.setGeometry(QtCore.QRect(50, 210, 90, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        font.setPointSize(12)
        self.label_tem.setFont(font)
        self.label_tem.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_tem.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_tem.setObjectName(_fromUtf8("label_tem"))
        self.label_lat = QtGui.QLabel(Form)
        self.label_lat.setGeometry(QtCore.QRect(250, 270, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        self.label_lat.setFont(font)
        self.label_lat.setObjectName(_fromUtf8("label_lat"))
        self.lineEdit_long = QtGui.QLineEdit(Form)
        self.lineEdit_long.setGeometry(QtCore.QRect(140, 270, 90, 23))
        self.lineEdit_long.setObjectName(_fromUtf8("lineEdit_long"))
        self.lineEdit_lat = QtGui.QLineEdit(Form)
        self.lineEdit_lat.setGeometry(QtCore.QRect(330, 270, 90, 23))
        self.lineEdit_lat.setObjectName(_fromUtf8("lineEdit_lat"))
        self.label_location = QtGui.QLabel(Form)
        self.label_location.setGeometry(QtCore.QRect(30, 230, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_location.setFont(font)
        self.label_location.setObjectName(_fromUtf8("label_location"))
        self.Labelconfigure = QtGui.QLabel(Form)
        self.Labelconfigure.setGeometry(QtCore.QRect(30, 70, 131, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.Labelconfigure.setFont(font)
        self.Labelconfigure.setObjectName(_fromUtf8("Labelconfigure"))
        self.lineEditserver = QtGui.QLineEdit(Form)
        self.lineEditserver.setGeometry(QtCore.QRect(140, 110, 151, 23))
        self.lineEditserver.setText(_fromUtf8(""))
        self.lineEditserver.setObjectName(_fromUtf8("lineEditserver"))
        self.Labelserver = QtGui.QLabel(Form)
        self.Labelserver.setGeometry(QtCore.QRect(40, 110, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        self.Labelserver.setFont(font)
        self.Labelserver.setObjectName(_fromUtf8("Labelserver"))
        self.lineEditrobotID = QtGui.QLineEdit(Form)
        self.lineEditrobotID.setGeometry(QtCore.QRect(140, 140, 51, 23))
        self.lineEditrobotID.setText(_fromUtf8(""))
        self.lineEditrobotID.setObjectName(_fromUtf8("lineEditrobotID"))
        self.LabelrobotID = QtGui.QLabel(Form)
        self.LabelrobotID.setGeometry(QtCore.QRect(40, 140, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Mono"))
        self.LabelrobotID.setFont(font)
        self.LabelrobotID.setObjectName(_fromUtf8("LabelrobotID"))
        self.labelmap = QtGui.QLabel(Form)
        self.labelmap.setGeometry(QtCore.QRect(50, 310, 410, 410))
        self.labelmap.setText(_fromUtf8(""))
        self.labelmap.setObjectName(_fromUtf8("labelmap"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(240, 140, 50, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.ButtonExit = QtGui.QPushButton(Form)
        self.ButtonExit.setGeometry(QtCore.QRect(430, 712, 57, 23))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setItalic(True)
        self.ButtonExit.setFont(font)
        self.ButtonExit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ButtonExit.setObjectName(_fromUtf8("ButtonExit"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.ButtonExit, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.header.setText(_translate("Form", "THE MONITOR PANEL", None))
        self.label_env.setText(_translate("Form", "Environment", None))
        self.label_hum.setText(_translate("Form", "Humidity", None))
        self.label_long.setText(_translate("Form", "Longitude", None))
        self.label_tem.setText(_translate("Form", "Temperature", None))
        self.label_lat.setText(_translate("Form", "Latitude", None))
        self.label_location.setText(_translate("Form", "Location", None))
        self.Labelconfigure.setText(_translate("Form", "Configuration", None))
        self.Labelserver.setText(_translate("Form", "Cloud Server", None))
        self.LabelrobotID.setText(_translate("Form", "Robot ID", None))
        self.pushButton.setText(_translate("Form", "OK", None))
        self.ButtonExit.setText(_translate("Form", "EXIT", None))

class mywindow(QtGui.QWidget,Ui_Form):    
    def __init__(self):    
        super(mywindow,self).__init__()    
        self.setupUi(self)  #(self)这里理解为传入的参数是类mywindow的实例
        # interface = unicode(self.lineEditserver.text())
        # robotID = unicode(self.lineEditrobotID.text())
        global exo_id
        topic_name = "store_topic_"+exo_id
        #订阅关节角度信息
        rospy.Subscriber(topic_name,env_and_angle,self.callback)
        self.pushButton.clicked.connect(self.map_display)
    def callback(self,data):
         global leftk
         global lefth
         global rightk
         global righth
         global atmo
         global temp
         global hum
         global longitude
         global latitude
         global exo_id
         atmo = data.atmo
         hum = data.hum
         temp = data.temp
         leftk=data.leftk
         lefth=data.lefth
         rightk=data.rightk
         righth=data.righth   
         longitude=data.longitude
         latitude=data.latitude
         #display data
         self.lineEdit_tem.setText(str(temp))
         self.lineEdit_hum.setText(str(hum))
         self.lineEdit_long.setText(str(longitude))
         self.lineEdit_lat.setText(str(latitude))

    def map_display(self):
        global longitude
        global latitude
        #在线模式
        # url="http://api.map.baidu.com/staticimage/v2?ak=deORyDWtAUIuqAOYN7O6f7ikELN2tsD9&center="+str(longitude)+","+str(latitude)+"&zoom=18&markers="+str(longitude)+","+str(latitude)
        # urllib.urlretrieve(url,"/home/ubuntu/NeuExoMap/mymap.png")
        #离线模式
        gd_lng = longitude
        gd_lat = latitude
        (tileX, tileY) = sign.GeographyToTile(gd_lng, gd_lat)  # 获取瓦片坐标
        (pixelX_init, pixelY_init) = sign.GeographyToPixel(gd_lng, gd_lat)  # 获取像素坐标
        (numX, numY, tileX_init, tileY_init) = sign.TileJudge(tileX, tileY)  # 判断瓦片落在哪一个部分,返回这个部分的左上角的瓦片坐标
        (pixelX, pixelY) = (pixelX_init + (int(tileX) - tileX_init) * 256, pixelY_init + (int(tileY) - tileY_init) * 256)  # 计算在该部分瓦片的像素坐标
        img = cv2.imread(pre_path+"/neu_tiles/" + str(numX) + "_" + str(numY) + "/tile_png/L18/neu.png")
        cv2.circle(img, (int(round(pixelX)), int(round(pixelY))), 10, (0, 0, 255), -1)
        img = cv2.resize(img,(400,400),interpolation=cv2.INTER_LINEAR)
        cv2.imwrite("/home/ros/NeuExoMap/mymap.png", img)
        image = QtGui.QImage("/home/ros/NeuExoMap/mymap.png")          
        self.labelmap.setPixmap(QtGui.QPixmap.fromImage(image))
        self.labelmap.adjustSize()

        screenshot = QtGui.QPixmap.grabWidget(Ui_Form)
        QtGui.QPainter.drawPixmap(screenshot)

if __name__=="__main__":  
    exo_id = str(sys.argv[1])
    node_name = "Monitor_"+exo_id
    rospy.init_node(node_name,anonymous = True)
    app=QtGui.QApplication(sys.argv)
    myshow=mywindow()  
    myshow.show()  
    sys.exit(app.exec_())