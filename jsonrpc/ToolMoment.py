import cv2
import numpy as np
from rsvconfig import RsvConfigure

class ToolMoment:
    def sobeled_img(self, img):
        img_gx = cv2.Sobel(img, cv2.CV_16S, 1, 0)
        img_gy = cv2.Sobel(img, cv2.CV_16S, 0, 1)
        img0_gx = cv2.convertScaleAbs(img_gx)
        img0_gy = cv2.convertScaleAbs(img_gy) 
        newimg = cv2.addWeighted(img0_gx, 0.5, img0_gy, 0.5, 0)
        return newimg
    
    def process_img(self, img):
        image = cv2.GaussianBlur(img, (5, 5), 0)
        image = self.sobeled_img(image)
        ret, binary = cv2.threshold(image, 10, 255, cv2.THRESH_BINARY)#|cv2.THRESH_OTSU)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel) 
#        cv2.imshow("oro",closed)
#        cv2.waitKey(10)
        return closed

    """利用轮廓矩进行物体识别与定位"""
    def ObtainExternalEdge(self, img):
        #ret, binary = cv2.threshold(img,60,255,cv2.THRESH_BINARY)#|cv2.THRESH_OTSU) 
        #闭运算  
        #closed = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, self.kernel)         
        closed = self.process_img(img)
        contours, hierarchy = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        return contours    
    
    def calculate_arc_params(self, cont):
        arclen = cv2.arcLength(cont, True)
        area = cv2.contourArea(cont, False)
        return arclen, area
        
    def __init__(self, template_image):
        self.m_configure = RsvConfigure()
        self.model = template_image
        self.kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
         
        self.contours_m = self.ObtainExternalEdge(template_image)
        max_edge = 0
        self.max_edge_index = 0
        for i in range(0, len(self.contours_m)):
            lens, areas = self.calculate_arc_params(self.contours_m[i])
            if lens > max_edge:
                self.max_edge_index = i
                max_edge = lens
        
        M = cv2.moments(self.contours_m[self.max_edge_index])
        self.angle0 = 28.647889756541*np.arctan2(2*M['mu11'], (M['mu20']-M['mu02']))
        self.arclen, self.area = self.calculate_arc_params(self.contours_m[self.max_edge_index])
        
   
    def FindObjects(self, _image, roi):
        image = _image[roi[1]:roi[1]+roi[3], roi[0]:roi[0]+roi[2]]
        contours_i = self.ObtainExternalEdge(image)
#==============================================================================
#        img = cv2.cvtColor(image,cv2.cv.CV_GRAY2BGR)
#        cv2.drawContours(img,contours_i,-1,(0,255,0),3)  
#        cv2.imshow("model",img)
#        cv2.waitKey(10)        
#==============================================================================
        objlist = []
        
        score = 0
        for i in range(np.array(contours_i).shape[0]):
            score = 1-cv2.matchShapes(self.contours_m[self.max_edge_index], contours_i[i], cv2.cv.CV_CONTOURS_MATCH_I1, 0.0)
            if score >= 0.8:
                #filter widht arc parameters
                flag = True
                arclen, area = self.calculate_arc_params(contours_i[i])
                if arclen > 1.2*self.arclen or arclen < 0.8*self.arclen:
                    flag = False
                if area > 1.2*self.area or area < 0.8*self.area :
                    flag = False
                
                if not flag:
                    continue
                
                M = cv2.moments(contours_i[i])
                x, y, w, h = cv2.boundingRect(contours_i[i])
                cx = x+0.5*w
                cy = y+0.5*h  
                cx = cx*self.m_configure.scale[0]
                cy = cy*self.m_configure.scale[1]
                angle = 0#28.647889756541*np.arctan2(2*M['mu11'],(M['mu20']-M['mu02']))-self.angle0
                objlist.append([cx + roi[0], cy + roi[1], angle, score, 0])
        return objlist

