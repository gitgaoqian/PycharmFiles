from bjsonrpc.handlers import BaseHandler
from bjsonrpc import createserver
from ipswitcher import swtichIP
from rsvconfig import RsvConfigure
from tasktools import buildModel
import cv2

m_configure = RsvConfigure()

class ServerHandler(BaseHandler):
    def save_config(self):
        m_configure.save()
        return "OK"

    def load_config(self):
        m_configure.load()
        return "OK"

    def set_json(self, config_string):
        m_configure.setstring(config_string)
        return "OK"

    def get_json(self):
        config_string= m_configure.getstring()
        return config_string

    def set_exp_time(self, value):
        m_configure.exposure_time = value
        return "OK"

    def set_contrast(self, value):
        m_configure.contrast = value
        return "OK"

    def set_brightness(self, value):
        m_configure.brightness = value
        return "OK"

    def set_resolution(self, width, height):
        m_configure.resolution = [width, height]
        return "OK"

    def set_color(self, value):
        m_configure.color_gray = value
        return "OK"

    def get_exp_time(self):
        return m_configure.exposure_time

    def get_contrast(self):
        return m_configure.contrast

    def get_brightness(self):
        return m_configure.brightness

    def get_resolution(self):
        return m_configure.resolution

    def get_color(self):
        return m_configure.color_gray

    # ---- Cropper Parameters -----#
    def set_roi(self,roi):
        m_configure.rect_roi = roi
        return "OK"

    def get_roi(self):
        return m_configure.rect_roi

    def get_model_roi(self):
        return m_configure.model_roi

    #list containing multiple objects for Finder
    def add_model(self,roi,name,thres,pyr,ang):
        m_configure.model_roi = roi
        m_configure.models.append(name+".jpg")
        m_configure.thresholds.append(thres)
        m_configure.pyramid_nums.append(pyr)
        m_configure.angle_ranges.append(ang)
        m_configure.model_number = len(m_configure.models)
        img = cv2.imread("current.jpg")
        crop_img = img[m_configure.model_roi[1]:m_configure.model_roi[1] + m_configure.model_roi[3], m_configure.model_roi[0]:m_configure.model_roi[0] + m_configure.model_roi[2]]
        filename = m_configure.models[-1]
        cv2.imwrite(filename, crop_img)
        
        m_configure.model_changed = True
        return "OK"

    def delete_model(self,n):
        del m_configure.models[n]
        del m_configure.thresholds[n]
        del m_configure.pyramid_nums[n]
        del m_configure.angle_ranges[n]
        m_configure.model_number = len(m_configure.models)
        
        m_configure.model_changed = True
        
        return "OK"

    def get_model_count(self):
        return m_configure.model_number

    def get_model_file(self,n):
        return m_configure.models[n]

    def get_model_threshold(self,n):
        return m_configure.thresholds[n]

    def get_model_pyramid_nums(self,n):
        return m_configure.pyramid_nums[n]

    def get_model_angle_range(self,n):
        return m_configure.angle_ranges[n]

    def set_model_threshold(self,n,value):
        m_configure.thresholds[n] = value
        m_configure.model_changed = True
        
        return "OK"

    def set_model_pyramid_nums(self,n,value):
        m_configure.pyramid_nums[n] = value
        
        m_configure.model_changed = True
        return "OK"

    def get_model_information(self,n):
        return m_configure.models[n],m_configure.angle_ranges[n],m_configure.pyramid_nums[n],m_configure.thresholds[n]

    def set_model_angle_range(self,n,value):
        m_configure.angle_ranges[n] = value
        
        m_configure.model_changed = True
        
        return "OK"

    def set_scale(self,value):
        m_configure.scale = value
        
        m_configure.model_changed = True
        
        return "OK"

    def get_scale(self):
        return m_configure.scale

    def set_prefix(self,value):
        m_configure.prefix = value
        return "OK"

    def get_prefix(self):
        return m_configure.prefix

    def set_wildcards(self, value):
        m_configure.wildcards = value
        return "OK"

    def get_wildcards(self):
        return m_configure.wildcards

    def set_middlefix(self, value):
        m_configure.middlefix = value
        return "OK"

    def get_middlefix(self):
        return m_configure.middlefix

    def set_postfix(self, value):
        m_configure.postfix = value
        return "OK"

    def get_postfix(self):
        return m_configure.postfix

    def get_restring(self):
        return m_configure.prefix,m_configure.postfix,m_configure.middlefix,m_configure.wildcards

    def set_disp_type(self, value):
        m_configure.disp_type = value
        return "OK"

    def get_disp_type(self):
        return m_configure.disp_type

    def set_marker(self, value):
        m_configure.marker = value
        return "OK"

    def get_marker(self):
        return m_configure.marker

    def set_color1(self, value):
        m_configure.color1 = value
        return "OK"

    def get_color1(self):
        return m_configure.color1

    def set_color2(self, value):
        m_configure.color2 = value
        return "OK"

    def get_color2(self):
        return m_configure.color2

    def set_timer_enable(self, value):
        m_configure.timer_enable = value
        return "OK"

    def get_timer_enable(self):
        return m_configure.timer_enable

    def set_timer_interval(self, value):
        m_configure.timer_interval = value
        return "OK"

    def get_timer_interval(self):
        return m_configure.timer_interval

    def set_io_enable(self, value):
        m_configure.io_enable = value
        return "OK"

    def get_io_enable(self):
        return m_configure.io_enable

    def set_io_logic(self, value):
        m_configure.io_logic = value
        return "OK"

    def get_io_logic(self):
        return m_configure.io_logic

    def set_io_filter(self, value):
        m_configure.io_filter = value
        return "OK"

    def get_io_filter(self):
        return m_configure.io_filter

    def set_interface(self, value):
        m_configure.interface = value
        return "OK"

    def get_interface(self):
        return m_configure.interface

    def set_uart_enable(self, value):
        m_configure.uart_enable = value
        return "OK"

    def get_uart_enable(self):
        return m_configure.uart_enable

    def set_uart_baudrate(self, value):
        m_configure.uart_baudrate = value
        return "OK"

    def get_uart_baudrate(self):
        return m_configure.uart_baudrate

    def set_dio_enable(self, value):
        m_configure.dio_enable = value
        return "OK"

    def get_dio_enable(self):
        return m_configure.dio_enable

    def set_dio_logic(self, value):
        m_configure.dio_logic = value
        return "OK"

    def get_dio_logic(self):
        return m_configure.dio_logic

    def set_socket_ip(self, value):
        m_configure.socket_ip = value
        return "OK"

    def get_socket_ip(self):
        return m_configure.socket_ip

    def set_socket_port(self, value):
        m_configure.socket_port = value
        return "OK"

    def get_socket_port(self):
        return m_configure.socket_port

    def set_socket_client_number(self, value):
        m_configure.socket_client_number = value
        return "OK"

    def get_socket_client_number(self):
        return m_configure.socket_client_number

    def set_socket_timeout(self, value):
        m_configure.socket_timeout = value
        return "OK"

    def get_socket_timeout(self):
        return m_configure.socket_timeout

    def set_socket_trig_string(self, value):
        m_configure.socket_trig_string = value
        return "OK"

    def get_socket_trig_string(self):
        return m_configure.socket_trig_string

    def set_task_mapper(self, value):
        m_configure.task_mapper = value
        return "OK"

    def get_task_mapper(self):
        return m_configure.task_mapper

    def trig(self):
        m_configure.rpc_trig = True
        return "OK"

    def set_eth0_ip(self,newip):
        m_configure.eth0_ip = newip
        print newip
        swtichIP(newip)
        return "OK"

    def get_eth0_ip(self):
        return m_configure.eth0_ip

rpcserver = createserver(host="0.0.0.0", handler_factory=ServerHandler)
