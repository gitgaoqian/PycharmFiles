#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 11:49:00 2016

@author: robot
"""
from threading import Timer
import  time
global time_interval
time_interval=0.01
################ROs needed########3
import rospy
from geometry_msgs.msg import Twist
#from geometry_msgs.msg import Point32
####################################
global right_elbow_display
global right_shoulder_1_display
global right_shoulder_2_display
global right_shoulder_3_display

global min_distance_right_arm
global min_distance_left_arm

min_distance_right_arm=0
min_distance_left_arm=0

right_elbow_display=0
right_shoulder_1_display=0
right_shoulder_2_display=0
right_shoulder_3_display=0

global  left_elbow_display
global  left_shoulder_1_display
global  left_shoulder_2_display
global  left_shoulder_3_display
left_elbow_display=0
left_shoulder_1_display=0
left_shoulder_2_display=0
left_shoulder_3_display=0



global my_tab_select
global flag  
flag=0      
global Left_elbow_joint_value
global Left_shoulder_joint_L_value
global Left_shoulder_joint_M_value
global Left_shoulder_joint_U_value
global Right_elbow_joint_value
global Right_shoulder_L_value
global Right_shoulder_M_value
global Right_shoulder_U_value
###############笛卡尔############
global Left_cartesian_x_value
global Left_cartesian_y_value
global Left_cartesian_z_value
global Right_cartesian_x_value
global Right_cartesian_y_value
global Right_cartesian_z_value

my_tab_select=0

Left_elbow_joint_value=60
Left_shoulder_joint_L_value=90
Left_shoulder_joint_M_value=15
Left_shoulder_joint_U_value=16
Right_elbow_joint_value=23
Right_shoulder_L_value=95
Right_shoulder_M_value=20
Right_shoulder_U_value=10
#########chushi
Left_cartesian_x_value=0.073*1000
Left_cartesian_y_value=0.5728*1000
Left_cartesian_z_value=0.15*1000
Right_cartesian_x_value=0.073*1000
Right_cartesian_y_value=0.5728*1000
Right_cartesian_z_value=0.15*1000

import sys
from PyQt4 import QtCore, QtGui
from imNEU import Ui_imneu_mainwindow 
class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_imneu_mainwindow()
        self.ui.setupUi(self)
        rospy.Subscriber('out_arm_left', Twist, self.callback_dispaly_left)
        rospy.Subscriber('out_arm_right', Twist, self.callback_display_right)
        #rospy.spin()
		# here we connect signals with our slots
        global my_tab_select
        my_tab_select=self.ui.tabWidget.currentIndex()
        global flag
        flag=0
        ################关节角度控制，设置滑块为信号，槽函数为显示滑块设置的角度值
        QtCore.QObject.connect(self.ui.left_elbow_joint,QtCore.SIGNAL("valueChanged(int)"), self.left_elbow_joint_get)
        QtCore.QObject.connect(self.ui.left_shoulder_joint_L,QtCore.SIGNAL("valueChanged(int)"), self.left_shoulder_joint_L_get)
        QtCore.QObject.connect(self.ui.left_shoulder_joint_M,QtCore.SIGNAL("valueChanged(int)"), self.left_shoulder_joint_M_get)
        QtCore.QObject.connect(self.ui.left_shoulder_joint_U,QtCore.SIGNAL("valueChanged(int)"), self.left_shoulder_joint_U_get)
        QtCore.QObject.connect(self.ui.right_elbow_joint,QtCore.SIGNAL("valueChanged(int)"), self.right_elbow_joint_get)
        QtCore.QObject.connect(self.ui.right_shoulder_L,QtCore.SIGNAL("valueChanged(int)"), self.right_shoulder_L_get)
        QtCore.QObject.connect(self.ui.right_shoulder_M,QtCore.SIGNAL("valueChanged(int)"), self.right_shoulder_M_get)
        QtCore.QObject.connect(self.ui.right_shoulder_U,QtCore.SIGNAL("valueChanged(int)"), self.right_shoulder_U_get)



        ###########################笛卡尔坐标控制################################################################
        QtCore.QObject.connect(self.ui.left_cartesian_x,QtCore.SIGNAL("valueChanged(int)"), self.left_cartesian_x_get)
        QtCore.QObject.connect(self.ui.left_cartesian_y,QtCore.SIGNAL("valueChanged(int)"), self.left_cartesian_y_get)
        QtCore.QObject.connect(self.ui.left_cartesian_z,QtCore.SIGNAL("valueChanged(int)"), self.left_cartesian_z_get)
        QtCore.QObject.connect(self.ui.right_cartesian_x,QtCore.SIGNAL("valueChanged(int)"), self.right_cartesian_x_get)
        QtCore.QObject.connect(self.ui.right_cartesian_y,QtCore.SIGNAL("valueChanged(int)"), self.right_cartesian_y_get)
        QtCore.QObject.connect(self.ui.right_cartesian_z,QtCore.SIGNAL("valueChanged(int)"), self.right_cartesian_z_get)
        #########################################关节角度控制复位############################3
        QtCore.QObject.connect(self.ui.joint_angle_reset_button,QtCore.SIGNAL("clicked()"), self.joint_angle_reset)
        #####################笛卡尔控制复位#####
        QtCore.QObject.connect(self.ui.cartesian_reset_button,QtCore.SIGNAL("clicked()"), self.cartesian_reset)
        ###########################################exccute button############################################
        QtCore.QObject.connect(self.ui.joint_angle_excute_button,QtCore.SIGNAL("clicked()"), self.joint_angle_excute)
        QtCore.QObject.connect(self.ui.cartesian_excute_button,QtCore.SIGNAL("clicked()"), self.cartesian_excute)
#################add for the hand control##########
        QtCore.QObject.connect(self.ui.hand_open,QtCore.SIGNAL("clicked()"), self.hand_open_excute)
        QtCore.QObject.connect(self.ui.hand_half_closed,QtCore.SIGNAL("clicked()"), self.hand_half_closed_excute)
        QtCore.QObject.connect(self.ui.hand_closed,QtCore.SIGNAL("clicked()"), self.hand_closed_excute)
        QtCore.QObject.connect(self.ui.fangzhi_zhunbei,QtCore.SIGNAL("clicked()"), self.fangzhi_zhunbei_excute)

        #######################################tab selector#######################################################\
        QtCore.QObject.connect(self.ui.tabWidget,QtCore.SIGNAL("currentChanged(int)"), self.tab_index_selector)
        if flag==0:
            self.ui.lineEdit_left_elbow.setText(str(60))
            self.ui.lineEdit_left_shoulder_L.setText(str(90)) 
            self.ui.lineEdit_left_shoulder_M.setText(str(15)) 
            self.ui.lineEdit_left_shoulder_U.setText(str(16)) 
            self.ui.lineEdit_right_elbow.setText(str(23)) 
            self.ui.lineEdit_right_shoulder_L.setText(str(95))
            self.ui.lineEdit_right_shoulder_M.setText(str(20))
            self.ui.lineEdit_right_shoulder_U.setText(str(10)) 
            
            self.ui.lineEdit_left_cartesian_x.setText(str(0.073))
            self.ui.lineEdit_left_cartesian_y.setText(str(-0.5728)) 
            self.ui.lineEdit_left_cartesian_z.setText(str(0.15)) 
            self.ui.lineEdit_right_cartesian_x.setText(str(0.073)) 
            self.ui.lineEdit_right_cartesian_y.setText(str(-0.5728)) 
            self.ui.lineEdit_right_cartesian_z.setText(str(-0.15))
            
#            self.ui.left_elbow_joint.setValue(60)
#            self.ui.left_shoulder_joint_L.setValue(90)
#            self.ui.left_shoulder_joint_M.setValue(15)
#            self.ui.left_shoulder_joint_U.setValue(16)
#            self.ui.right_elbow_joint.setValue(23)
#            self.ui.right_shoulder_L.setValue(95)
#            self.ui.right_shoulder_M.setValue(20)
#            self.ui.right_shoulder_U.setValue(10)
#            
#            self.ui.left_cartesian_x.setValue(0.073*1000)
#            self.ui.left_cartesian_y.setValue(int(-0.5728*1000))
#            self.ui.left_cartesian_z.setValue(0.15*1000)
#            self.ui.right_cartesian_x.setValue(0.073*1000)
#            self.ui.right_cartesian_y.setValue(int(-0.5728*1000))
#            self.ui.right_cartesian_z.setValue(int(-0.15*1000))            
            flag=1
    
#####################################################
		#QtCore.QObject.connect(self.ui.left_elbow_joint,QtCore.SIGNAL("valueChanged(int)"), self.left_elbow_joint_get)
		#QtCore.QObject.connect(self.ui.left_elbow_joint,QtCore.SIGNAL("valueChanged(int)"), self.left_elbow_joint_get)
  ###################tab_selector##############################
    def tab_index_selector(self):
        global my_tab_select
        #self.ui.editor_window.setText('aaaaaaaaaa')
        my_tab_select=self.ui.tabWidget.currentIndex()

  ###############################################reset function reset the value of every joint angle ############\
    def joint_angle_reset(self):
        #print "helo"
        self.ui.left_elbow_joint.setValue(60)
        time.sleep(0.03)
        self.ui.left_shoulder_joint_L.setValue(90)
        time.sleep(0.03)
        self.ui.left_shoulder_joint_M.setValue(15)
        time.sleep(0.03)
        self.ui.left_shoulder_joint_U.setValue(16)
        time.sleep(0.03)
        self.ui.right_elbow_joint.setValue(23)
        time.sleep(0.03)
        self.ui.right_shoulder_L.setValue(95)
        time.sleep(0.03)
        self.ui.right_shoulder_M.setValue(20)
        time.sleep(0.03)
        self.ui.right_shoulder_U.setValue(10)
        time.sleep(0.03)
##############################reset the cartestian value################################
    def cartesian_reset(self):
        self.ui.left_cartesian_x.setValue(int(0.073*1000))
        time.sleep(0.03)
        self.ui.left_cartesian_y.setValue(int(0.5728*1000))
        time.sleep(0.03)
        self.ui.left_cartesian_z.setValue(int(0.15*1000))
        time.sleep(0.03)
        self.ui.right_cartesian_x.setValue(int(0.073*1000))
        time.sleep(0.03)
        self.ui.right_cartesian_y.setValue(int(0.5728*1000))
        time.sleep(0.03)
        self.ui.right_cartesian_z.setValue(int(0.15*1000))
        time.sleep(0.03)
#        publish_cartesian()
################################excute the input angle in the  lineedit########################
    def joint_angle_excute(self):
       global Left_elbow_joint_value
       global Left_shoulder_joint_L_value
       global Left_shoulder_joint_M_value#使用global，表明对全局变量的引用
       global Left_shoulder_joint_U_value
       global Right_elbow_joint_value
       global Right_shoulder_L_value
       global Right_shoulder_M_value
       global Right_shoulder_U_value
       Left_elbow_joint_value =self.ui.lineEdit_left_elbow.text()#文本框中输入角度值
       Left_shoulder_joint_L_value=self.ui.lineEdit_left_shoulder_L.text()
       Left_shoulder_joint_M_value=self.ui.lineEdit_left_shoulder_M.text()
       Left_shoulder_joint_U_value=self.ui.lineEdit_left_shoulder_U.text()
       Right_elbow_joint_value=self.ui.lineEdit_right_elbow.text()
       Right_shoulder_L_value=self.ui.lineEdit_right_shoulder_L.text()
       Right_shoulder_M_value=self.ui.lineEdit_right_shoulder_M.text()
       Right_shoulder_U_value=self.ui.lineEdit_right_shoulder_U.text()
       
       self.ui.left_elbow_joint.setValue(int(Left_elbow_joint_value))#根据输入的角度值，滑块进行移动
       self.ui.left_shoulder_joint_L.setValue(int(Left_shoulder_joint_L_value))
       self.ui.left_shoulder_joint_M.setValue(int(Left_shoulder_joint_M_value))
       self.ui.left_shoulder_joint_U.setValue(int(Left_shoulder_joint_U_value))
       self.ui.right_elbow_joint.setValue(int(Right_elbow_joint_value))
       self.ui.right_shoulder_L.setValue(int(Right_shoulder_L_value))
       self.ui.right_shoulder_M.setValue(int(Right_shoulder_M_value))
       self.ui.right_shoulder_U.setValue(int(Right_shoulder_U_value))
######################cartesian_excute###################
    def cartesian_excute(self):
        global Left_cartesian_x_value
        global Left_cartesian_y_value
        global Left_cartesian_z_value
        global Right_cartesian_x_value
        global Right_cartesian_y_value
        global Right_cartesian_z_value
        Left_cartesian_x_value=abs(round(float(self.ui.lineEdit_left_cartesian_x.text())*1000))
        Left_cartesian_y_value=abs(round(float(self.ui.lineEdit_left_cartesian_y.text())*1000))
        Left_cartesian_z_value=abs(round(float(self.ui.lineEdit_left_cartesian_z.text())*1000))
        Right_cartesian_x_value=abs(round(float(self.ui.lineEdit_right_cartesian_x.text())*1000))
        Right_cartesian_y_value=abs(round(float(self.ui.lineEdit_right_cartesian_y.text())*1000))
        Right_cartesian_z_value=abs(round(float(self.ui.lineEdit_right_cartesian_z.text())*1000))
        
        self.ui.left_cartesian_x.setValue(int(float(Left_cartesian_x_value)))
        self.ui.left_cartesian_y.setValue(int(float(Left_cartesian_y_value)))
        self.ui.left_cartesian_z.setValue(int(float(Left_cartesian_z_value)))
        self.ui.right_cartesian_x.setValue(int(float(Right_cartesian_x_value)))
        self.ui.right_cartesian_y.setValue(int(float(Right_cartesian_y_value)))
        self.ui.right_cartesian_z.setValue(int(float(Right_cartesian_z_value)))
        #publish_cartesian()
        
##################################read the value of slider and set the line edit #############   
        
        #print Left_elbow_joint_value
    def left_elbow_joint_get(self):
        global Left_elbow_joint_value
        Left_elbow_joint_value=self.ui.left_elbow_joint.value()
        self.ui.lineEdit_left_elbow.setText(str(Left_elbow_joint_value))
        publish_joint_angle()
       # print "publish_joint_anglepublish_joint_anglepublish_joint_angle"
    def left_shoulder_joint_L_get(self):
        global Left_shoulder_joint_L_value
        Left_shoulder_joint_L_value=self.ui.left_shoulder_joint_L.value()
        self.ui.lineEdit_left_shoulder_L.setText(str(Left_shoulder_joint_L_value))         
        publish_joint_angle()
        #print "publish_joint_anglepublish_joint_anglepublish_joint_angle"
        
    def left_shoulder_joint_M_get(self):
        global Left_shoulder_joint_M_value
        Left_shoulder_joint_M_value=self.ui.left_shoulder_joint_M.value()
        self.ui.lineEdit_left_shoulder_M.setText(str(Left_shoulder_joint_M_value)) 
        publish_joint_angle()
        #print "publish_joint_anglepublish_joint_anglepublish_joint_angle"       
    def left_shoulder_joint_U_get(self):
        global Left_shoulder_joint_U_value
        Left_shoulder_joint_U_value=self.ui.left_shoulder_joint_U.value()
        self.ui.lineEdit_left_shoulder_U.setText(str(Left_shoulder_joint_U_value)) 
        publish_joint_angle()
        #print "publish_joint_anglepublish_joint_anglepublish_joint_angle"        
    def right_elbow_joint_get(self):
        global Right_elbow_joint_value
        Right_elbow_joint_value=self.ui.right_elbow_joint.value()
        self.ui.lineEdit_right_elbow.setText(str(Right_elbow_joint_value)) 
        publish_joint_angle()
       # print "publish_joint_anglepublish_joint_anglepublish_joint_angle"    
    def right_shoulder_L_get(self):
        global Right_shoulder_L_value
        Right_shoulder_L_value=self.ui.right_shoulder_L.value()
        self.ui.lineEdit_right_shoulder_L.setText(str(Right_shoulder_L_value))
        publish_joint_angle()
        #print "publish_joint_anglepublish_joint_anglepublish_joint_angle"        
        
    def right_shoulder_M_get(self):
        global Right_shoulder_M_value
        Right_shoulder_M_value=self.ui.right_shoulder_M.value()
        self.ui.lineEdit_right_shoulder_M.setText(str(Right_shoulder_M_value))
        publish_joint_angle()
        #print "publish_joint_anglepublish_joint_anglepublish_joint_angle"        
    def right_shoulder_U_get(self):
        global Right_shoulder_U_value
        Right_shoulder_U_value=self.ui.right_shoulder_U.value()
        self.ui.lineEdit_right_shoulder_U.setText(str(Right_shoulder_U_value))
        publish_joint_angle()
       # print "publish_joint_anglepublish_joint_anglepublish_joint_angle"
###################笛卡尔##############  
    def left_cartesian_x_get(self):
        global Left_cartesian_x_value
        Left_cartesian_x_value=self.ui.left_cartesian_x.value()
        self.ui.lineEdit_left_cartesian_x.setText(str(float(Left_cartesian_x_value)/1000)) 
        publish_cartesian()
       # print "publish_cartesianpublish_cartesianpublish_cartesian"  
    def left_cartesian_y_get(self):
        global Left_cartesian_y_value
        Left_cartesian_y_value=self.ui.left_cartesian_y.value()
        self.ui.lineEdit_left_cartesian_y.setText(str(float(-1*Left_cartesian_y_value)/1000))
        publish_cartesian()
       # print "publish_cartesianpublish_cartesianpublish_cartesian"
        
    def left_cartesian_z_get(self):
        global Left_cartesian_z_value
        Left_cartesian_z_value=self.ui.left_cartesian_z.value()
        self.ui.lineEdit_left_cartesian_z.setText(str(float(Left_cartesian_z_value)/1000))
        publish_cartesian()
        #print "publish_cartesianpublish_cartesianpublish_cartesian"

        
    def right_cartesian_x_get(self):
        global Right_cartesian_x_value
        Right_cartesian_x_value=self.ui.right_cartesian_x.value()
        self.ui.lineEdit_right_cartesian_x.setText(str(float(Right_cartesian_x_value)/1000))
        publish_cartesian()
        #print "publish_cartesianpublish_cartesianpublish_cartesian"

        
    def right_cartesian_y_get(self):
        global Right_cartesian_y_value
        Right_cartesian_y_value=self.ui.right_cartesian_y.value()
        self.ui.lineEdit_right_cartesian_y.setText(str(float(-1*Right_cartesian_y_value)/1000))
        publish_cartesian()
       # print "publish_cartesianpublish_cartesianpublish_cartesian"
        
    def right_cartesian_z_get(self):
        global Right_cartesian_z_value
        Right_cartesian_z_value=self.ui.right_cartesian_z.value()
        self.ui.lineEdit_right_cartesian_z.setText(str(float(-1*Right_cartesian_z_value)/1000))
        publish_cartesian()
        #print "publish_cartesianpublish_cartesianpublish_cartesian" 
    def callback_dispaly_left(self,left_arm_twist):
        if  my_tab_select==1: 
            global  left_elbow_display
            global  left_shoulder_1_display
            global  left_shoulder_2_display
            global  left_shoulder_3_display
            global  min_distance_left_arm
            left_elbow_display=left_arm_twist.linear.x  
            left_shoulder_1_display=left_arm_twist.linear.y
            left_shoulder_2_display=left_arm_twist.linear.z
            left_shoulder_3_display=left_arm_twist.angular.x
        
            min_distance_left_arm=left_arm_twist.angular.y
#        self.ui.lineEdit_left_elbow_display.setText(str(float(left_elbow_display))
#        self.ui.lineEdit_left_shoulder1_display.setText(str(float(left_shoulder_1_display))
#        self.ui.lineEdit_left_shoulder2_display.setText(str(float(left_shoulder_2_display))  
#        self.ui.lineEdit_left_shoulder3_display.setText(str(float(left_shoulder_3_display))
            self.ui.lineEdit_left_elbow_display.setText(str(int(left_elbow_display)))
            self.ui.lineEdit_left_shoulder1_display.setText(str(int(left_shoulder_1_display)))
            self.ui.lineEdit_left_shoulder2_display.setText(str(int(left_shoulder_2_display)))  
            self.ui.lineEdit_left_shoulder3_display.setText(str(int(left_shoulder_3_display)))
            self.ui.lineEdit_mindistance_left.setText(str(float("%.2f" %min_distance_left_arm)))
    def callback_display_right(self,right_arm_twist):
        if  my_tab_select==1:
            global right_elbow_display
            global right_shoulder_1_display
            global right_shoulder_2_display
            global right_shoulder_3_display
            global min_distance_right_arm
            right_elbow_display=right_arm_twist.linear.x  
            right_shoulder_1_display=right_arm_twist.linear.y
            right_shoulder_2_display=right_arm_twist.linear.z
            right_shoulder_3_display=right_arm_twist.angular.x 

            min_distance_right_arm=right_arm_twist.angular.y
#        self.ui.lineEdit_right_elbow_display.setText(str(float(right_elbow_display))
#        self.ui.lineEdit_right_shoulder1_display.setText(str(float(right_shoulder_1_display))
#        self.ui.lineEdit_right_shoulder2_display.setText(str(float(right_shoulder_2_display))
#        self.ui.lineEdit_right_shoulder3_display.setText(str(float(right_shoulder_3_display))
            self.ui.lineEdit_right_elbow_display.setText(str(int(right_elbow_display)))
            self.ui.lineEdit_right_shoulder1_display.setText(str(int(right_shoulder_1_display)))
            self.ui.lineEdit_right_shoulder2_display.setText(str(int(right_shoulder_2_display)))
            self.ui.lineEdit_right_shoulder3_display.setText(str(int(right_shoulder_3_display)))
            self.ui.lineEdit_min_distance_right.setText(str(float("%.2f" %min_distance_right_arm)))
# 
    def hand_open_excute(self):
        left_hand_twist=Twist()
        left_hand_twist.linear.x=25
        left_hand_twist.linear.y=5
        left_hand_twist.linear.z=10
        left_hand_twist.angular.x=5
        left_hand_twist.angular.y=25
        left_hand_twist.angular.z=140    
        pub_hand_left_gesture.publish(left_hand_twist)
    def hand_half_closed_excute(self):
        left_hand_twist=Twist()
        left_hand_twist.linear.x=80
        left_hand_twist.linear.y=60
        left_hand_twist.linear.z=50
        left_hand_twist.angular.x=20
        left_hand_twist.angular.y=25
        left_hand_twist.angular.z=90   
        pub_hand_left_gesture.publish(left_hand_twist)   
    def hand_closed_excute(self):
        left_hand_twist=Twist()
        left_hand_twist.linear.x=100
        left_hand_twist.linear.y=150
        left_hand_twist.linear.z=145
        left_hand_twist.angular.x=125
        left_hand_twist.angular.y=160
        left_hand_twist.angular.z=80   
        pub_hand_left_gesture.publish(left_hand_twist) 
    def fangzhi_zhunbei_excute(self):
        fangzhi_zhunbei_twist=Twist()
        fangzhi_zhunbei_twist.linear.x=100
        fangzhi_zhunbei_twist.linear.y=150
        fangzhi_zhunbei_twist.linear.z=145
        fangzhi_zhunbei_twist.angular.x=125
        fangzhi_zhunbei_twist.angular.y=160
        fangzhi_zhunbei_twist.angular.z=140   
        pub_hand_left_gesture.publish(fangzhi_zhunbei_twist)         
def publish_cartesian():   
    global Left_cartesian_x_value
    global Left_cartesian_y_value
    global Left_cartesian_z_value
    global Right_cartesian_x_value
    global Right_cartesian_y_value
    global Right_cartesian_z_value    
    global left_cartesian_twist
    global right_cartesian_twist
    left_cartesian_twist=Twist()
    right_cartesian_twist=Twist()
    if  my_tab_select==1: 
        global pub_cartesian_leftarm
        global pub_cartesian_rightarm
        left_cartesian_twist.linear.x=float(float(Left_cartesian_x_value)/1000)
        left_cartesian_twist.linear.y=-float(float(Left_cartesian_y_value)/1000)
        left_cartesian_twist.linear.z=float(float(Left_cartesian_z_value)/1000)
    
        right_cartesian_twist.linear.x=float(float(Right_cartesian_x_value)/1000)
        right_cartesian_twist.linear.y=-float(float(Right_cartesian_y_value)/1000)
        right_cartesian_twist.linear.z=-float(float(Right_cartesian_z_value)/1000)
        try:
            #print "11111111111111111111111111111111111"
            pub_cartesian_leftarm.publish(left_cartesian_twist)
            pub_cartesian_rightarm.publish(right_cartesian_twist)
            global rate
            rate.sleep()
            #print  left_cartesian_twist.linear.x
        except KeyboardInterrupt:
            print"shutdown"
#        global t
#        t=Timer(time_interval,get_realtime_value)
#        t.start()

###############################################################################################        
#def get_realtime_value():
#    global Left_elbow_joint_value
#    global Left_shoulder_joint_L_value
#    global Left_shoulder_joint_M_value
#    global Left_shoulder_joint_U_value
#    global Right_elbow_joint_value
#    global Right_shoulder_L_value
#    global Right_shoulder_M_value
#    global Right_shoulder_U_value
#    
#    ############笛卡尔############
#    global Left_cartesian_x_value
#    global Left_cartesian_y_value
#    global Left_cartesian_z_value
#    global Right_cartesian_x_value
#    global Right_cartesian_y_value
#    global Right_cartesian_z_value
#    global my_tab_select
    

    

def publish_joint_angle():
    global Twist_imneu_leftarm
    Twist_imneu_leftarm=Twist()
    global Twist_imneu_rightarm
    Twist_imneu_rightarm=Twist()  
    global Left_elbow_joint_value
    global Left_shoulder_joint_L_value
    global Left_shoulder_joint_M_value
    global Left_shoulder_joint_U_value
    global Right_elbow_joint_value
    global Right_shoulder_L_value
    global Right_shoulder_M_value
    global Right_shoulder_U_value
    global my_tab_select
    if  my_tab_select==0:
        Twist_imneu_leftarm.linear.x=int(Left_elbow_joint_value)
        Twist_imneu_leftarm.linear.y=int(Left_shoulder_joint_L_value)
        Twist_imneu_leftarm.linear.z=int(Left_shoulder_joint_M_value)
        Twist_imneu_leftarm.angular.x=int(Left_shoulder_joint_U_value)
    
        Twist_imneu_rightarm.linear.x=int(Right_elbow_joint_value)
        Twist_imneu_rightarm.linear.y=int(Right_shoulder_L_value)
        Twist_imneu_rightarm.linear.z=int(Right_shoulder_M_value)
        Twist_imneu_rightarm.angular.x=int(Right_shoulder_U_value)
        try:
           # print"0000000000000000000000000000000"
            #rospy.spin()
            pub_leftarm.publish(Twist_imneu_leftarm)
            pub_rightarm.publish(Twist_imneu_rightarm)
           # print Twist_imneu_leftarm.linear.x
            global rate
            rate.sleep()
        except KeyboardInterrupt:
            print"shutdown"
#        global t
#        t=Timer(time_interval,get_realtime_value)
#        t.start()

    
     
if __name__ == "__main__":
    global my_tab_select
    rospy.init_node("joint_control_public",anonymous=True)
    pub_leftarm=rospy.Publisher("out_arm_left",Twist,queue_size=1000)#关节角度控制的左臂发布者
    pub_rightarm=rospy.Publisher("out_arm_right",Twist,queue_size=1000)#关节角度控制的右臂发布者
    pub_cartesian_leftarm=rospy.Publisher("in_arm_left",Twist,queue_size=1000) #笛卡尔控制的左臂发布者
    pub_cartesian_rightarm=rospy.Publisher("in_arm_right",Twist,queue_size=1000)#笛卡尔控制的左臂发布者
    
    pub_hand_left_gesture=rospy.Publisher("out_hand_left",Twist,queue_size=1000)#左臂特定的控制姿态   
    

    #rospy.spin()
    global rate
    rate=rospy.Rate(10)
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
#    t=Timer(time_interval,get_realtime_value)
#    t.start()
    myapp.show()
    #print int(Left_elbow_joint_value)
    sys.exit(app.exec_())

        ##############ROS public needed############         


 
    
