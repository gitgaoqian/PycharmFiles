# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 00:46:20 2016

@author: 程红太
"""
from rpcserver import *
from imutils.video.pivideostream import PiVideoStream
from ToolMoment import ToolMoment
from TCPServer import TCPServer
import cv2
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
import thread
import time


global video_capturer

class TestHTTPHandle(BaseHTTPRequestHandler):
    def do_GET(self):
        global video_capturer
        global video_busy
        # the default setting is for the live video, others are for the model
        if self.path == '/':
            while video_busy:
                time.sleep(0.001)
            video_busy = True
            image = video_capturer.read()
            video_busy = False
            ret, jpeg = cv2.imencode('.jpg', image, [int(cv2.IMWRITE_JPEG_QUALITY), 60])
            self.protocal_version = "HTTP/1.1"
            self.send_response(200)
            self.send_header("Welcome", "OK")
            self.end_headers()
            self.wfile.write(jpeg.tostring())

        elif self.path == '/test_algorithm':
            m_configure.http_trig = True
            self.protocal_version = "HTTP/1.1"
            self.send_response(200)
            self.send_header("Welcome", "OK")
            self.end_headers()
        elif self.path == '/favicon.ico':
            self.protocal_version = "HTTP/1.1"
            self.send_response(200)
            self.send_header("Welcome", "OK")
            self.end_headers()
        elif self.path == '/save':
            while video_busy:
                time.sleep(0.001)
            video_busy = True
            image = video_capturer.read()
            video_busy = False
            cv2.imwrite('current.jpg',image)
            
            self.protocal_version = "HTTP/1.1"
            self.send_response(200)
            self.send_header("Welcome", "OK")
            self.end_headers()            
        else:
            filename = self.path[1:]
            self.protocal_version = "HTTP/1.1"
            self.send_response(200)
            self.send_header("Welcome", "OK")
            self.end_headers()
            model = cv2.imread(filename)
            ret, jpeg = cv2.imencode('.jpg', model, [int(cv2.IMWRITE_JPEG_QUALITY), 60])
            self.wfile.write(jpeg.tostring())


def start_server(port):
    web_server = HTTPServer(('0.0.0.0', int(port)), TestHTTPHandle)
    print "Start HTTP Service on port 3001"
    print "==============================="
    web_server.serve_forever()  # 设置一直监听并接收请求,其中，IP为给localhost设定的访问地址


def thread_rsvtask():
    global ts
    global QuitFlag
    global video_capturer
    global video_busy
    global tool_busy

    while not QuitFlag:
        if m_configure.model_changed :
            print 'model changed!'
            
            
        if m_configure.rpc_trig or m_configure.tcp_trig or m_configure.uart_trig or m_configure.io_trig or m_configure.timer_trig or m_configure.http_trig:
            print "triged"
            m_configure.rpc_trig = False
            m_configure.tcp_trig = False
            m_configure.uart_trig = False
            m_configure.io_trig = False
            m_configure.timer_trig = False
            m_configure.http_trig = False

            while video_busy:
                time.sleep(0.001)
            video_busy = True

            img = video_capturer.read()
            video_busy = False
            img = cv2.cvtColor(img, cv2.cv.CV_BGR2GRAY)

            while tool_busy:
                time.sleep(0.001)
            tool_busy=True
            objlist = tm.FindObjects(img,m_configure.rect_roi)
            tool_busy = False

            ts.SocketTransfer(objlist)
        time.sleep(0.001)

if __name__ == "__main__":
    global ts
    global tm
    global QuitFlag
    global video_capturer
    global video_busy
    global tool_busy
    video_busy = False
    tool_busy = False
    QuitFlag = False
    print "starting the services......"
    model = cv2.imread("black.jpg", cv2.IMREAD_GRAYSCALE)
    tm = ToolMoment(model)
    
    video_capturer = PiVideoStream((640, 480), 20)
    video_capturer.start()
    print 'waiting for the image to steady'

##
##    video_capturer.camera.contrast = m_configure.contrast
##    video_capturer.camera.brightness = m_configure.brightness
##    video_capturer.camera.shutter_speed = m_configure.exposure_time
##    video_capturer.camera.exposure_mode = "auto"
    
    time.sleep(2.0)
        
    
    ts = TCPServer("0.0.0.0", 3000)
    print "URL: socket://localhost:3000 for data"
    thread.start_new_thread(start_server, (30000,))
    print "URL: http://localhost:30000 for web"
    thread.start_new_thread(thread_rsvtask, ())
    print "RSV: starting the vision task..."
##    print "URL: http://localhost:30001 for jsonrpc"
##    try:
##        http_server.serve_forever()
##    except KeyboardInterrupt:
##        QuitFlag = True
##        http_server.shutdown()
##    print "Stopping HTTP server ..."
    rpcserver.serve()
##    while 1:
##        time.sleep(1)
##        print "Stopping HTTP server ..."
        



