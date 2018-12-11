# -*- coding: utf-8 -*-
import cv2
import cv2.cv as cv
import numpy as np
import ctypes
from ctypes import *

class CvSize(Structure):
    _fields_ = [("height", c_int), ("width", c_int)]

class  ObjectInfo(Structure):
    pass

ObjectInfo._fields_ = [("id", c_int),
                       ("x", c_float),
                       ("y", c_float),
                       ("angle", c_float),
                       ("value", c_float)]

class TemplateMatch:
    def __init__(self, model_image):
        model_image = cv2.imread('D:\\2017\\0330m.png')  # 512 x 512
        model_image = np.array(model_image)
        model_step = model_image.dtype.itemsize * 3 * model_image.shape[1]
        model_size = CvSize(model_image.shape[1], model_image.shape[0])
        model_data = model_image.ctypes.data_as(ctypes.POINTER(ctypes.c_void_p)).contents
        dll = ctypes.WinDLL("D:\\2017\\20170620\\Debug\\20170620.dll")
        load_model = dll.LoadModel
        load_model.argtype = [CvSize, c_int, c_int, c_void_p, c_int]
        load_model(CvSize(model_size.height, model_size.width), cv.IPL_DEPTH_8U, 3, ctypes.byref(model_data),
                  model_step)


    def FindObjects(self, _image, roi):
        test_image = _image[roi[1]:roi[1] + roi[3], roi[0]:roi[0] + roi[2]]
        #test_image = cv2.imread('D:\\2017\\0330t.png')  # 512 x 512
        test_image = np.array(test_image)
        test_step = test_image.dtype.itemsize * 3 * test_image.shape[1]
        test_size = CvSize(test_image.shape[1], test_image.shape[0])
        test_data = test_image.ctypes.data_as(ctypes.POINTER(ctypes.c_void_p)).contents

        MatchTemplate = dll.DetectObjects #轮廓匹配
        MatchTemplate.argtype = [CvSize, c_int, c_int, c_void_p, c_int]
        MatchTemplate.restype = c_int
        num = MatchTemplate(CvSize(test_size.height, test_size.width), cv.IPL_DEPTH_8U, 3, ctypes.byref(test_data), test_step)

        FindingResults = dll.Results
        FindingResults.argtype = [c_int]
        FindingResults.restype = POINTER(ObjectInfo)
        for i in range(num):
            res = img_load2(i)
            print res.id, res.contents.x, res.contents.y, res.contents.angle, res.contents.value

