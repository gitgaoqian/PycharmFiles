import json
import os

class RsvConfigure:
    exposure_time = 0
    contrast = 50
    brightness = 50
    resolution = [640, 480]
    color_gray = False

    rect_roi=[0,0,640,480]
    model_roi=[0,0,640,480]

    #list containing multiple objects for Finder
    model_number = 0
    models = []
    thresholds = [0.8]
    pyramid_nums = [3]
    angle_ranges = [180]
    scale =[1.0,1.0]
    model_changed = False
    prefix = "["
    wildcards= "[%x,%y,%a,%i]"
    middlefix = ","
    postfix = "]"

    disp_type = 1
    marker = 1
    color1 = [1,0,0]
    color2 = [0,1,0]

    timer_enable = False
    timer_interval = 500

    io_enable = False
    io_logic  = True
    io_filter = 3

    interface = 1   #1 ethernet, 2 uart, 3 dio

    uart_enable = False
    uart_baudrate = 9600

    dio_enable = False
    dio_logic = True

    eth0_ip = "192.168.200.3"
    socket_ip = "0.0.0.0"
    socket_port = 3000
    socket_client_number = 1
    socket_timeout = 1000
    socket_trig_string = "Trig"

    task_mapper = 1 #default geometric model finder

    rpc_trig = False
    tcp_trig = False
    uart_trig = False
    io_trig = False
    timer_trig = False
    http_trig = False

    def __init__(self):
        self.load()

    def save(self):
        config_string=self.getstring()
        f=open("rsv.ini","w")
        f.write(config_string)
        f.close()

    def getstring(self):
        dic = {"exposure_time": self.exposure_time, "contrast": self.contrast, "brightness": self.brightness,
               "resolution": self.resolution, "color_gray": self.color_gray, "rect_roi": self.rect_roi,
               "model_roi": self.model_roi, "model_number": self.model_number, "models": self.models,
               "thresholds": self.thresholds, "pyramid_nums": self.pyramid_nums, "angle_ranges": self.angle_ranges,
               "scale": self.scale,
               "prefix": self.prefix, "wildcards": self.wildcards, "middlefix": self.middlefix, "postfix": self.postfix,
               "disp_type": self.disp_type, "marker": self.marker, "color1": self.color1, "color2": self.color2,
               "timer_enable": self.timer_enable, "timer_interval": self.timer_interval, "io_enable": self.io_enable,
               "io_logic": self.io_logic, "io_filter": self.io_filter, "interface": self.interface,
               "uart_enable": self.uart_enable, "uart_baudrate": self.uart_baudrate, "dio_enable": self.dio_enable,
               "dio_logic": self.dio_logic, "socket_ip": self.socket_ip, "socket_port": self.socket_port,
               "socket_client_number": self.socket_client_number, "socket_timeout": self.socket_timeout,
               "socket_trig_string": self.socket_trig_string, "task_mapper": self.task_mapper, "eth0_ip":self.eth0_ip}
        config_string = json.dumps(dic)
        return config_string

    def setstring(self,config_string):
        dic = json.loads(config_string)
        self.exposure_time = dic['exposure_time']
        self.contrast = dic['contrast']
        self.brightness = dic['brightness']
        self.resolution = dic['resolution']
        self.color_gray = dic['color_gray']
        self.rect_roi = dic['rect_roi']
        self.model_roi = dic['model_roi']
        self.model_number = dic['model_number']
        self.models = dic['models']
        self.thresholds = dic['thresholds']
        self.pyramid_nums = dic['pyramid_nums']
        self.scale = dic['scale']
        self.angle_ranges = dic['angle_ranges']
        self.prefix = dic['prefix']
        self.wildcards = dic['wildcards']
        self.middlefix = dic['middlefix']
        self.postfix = dic['postfix']
        self.disp_type = dic['disp_type']
        self.marker = dic['marker']
        self.color1 = dic['color1']
        self.color2 = dic['color2']
        self.timer_enable = dic['timer_enable']
        self.timer_interval = dic['timer_interval']
        self.io_enable = dic['io_enable']
        self.io_logic = dic['io_logic']
        self.io_filter = dic['io_filter']
        self.interface = dic['interface']
        self.uart_enable = dic['uart_enable']
        self.uart_baudrate = dic['uart_baudrate']
        self.dio_enable = dic['dio_enable']
        self.dio_logic = dic['dio_logic']
        self.socket_ip = dic['socket_ip']
        self.socket_port = dic['socket_port']
        self.socket_client_number = dic['socket_client_number']
        self.socket_timeout = dic['socket_timeout']
        self.socket_trig_string = dic['socket_trig_string']
        self.task_mapper = dic['task_mapper']
        self.eth0_ip = dic['eth0_ip']

    def load(self):
        if os.path.exists("rsv.ini"):
            f=open("rsv.ini","r")
            config_string=f.read()
            f.close()
            self.setstring(config_string)
        else:
            self.save()