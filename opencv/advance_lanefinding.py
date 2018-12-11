#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:ros
# import some libs we need
import numpy as np
import cv2
import glob
import matplotlib.pyplot as plt
from moviepy.editor import VideoFileClip
from IPython.display import HTML
from collections import deque


#Display
showMe = 0
def display(img,title,color=1):
    '''
    func:display image
    img: rgb or grayscale
    title:figure title
    color:show image in color(1) or grayscale(0)
    '''
    if color:
        plt.imshow(img)
    else:
        plt.imshow(img,cmap='gray')
    plt.title(title)
    plt.axis('off')
    plt.show()
def grayscale(img):
    '''
    灰度转换，返回只有一个颜色通道的图像
    '''
    return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # if you read an image with cv.imread(),return cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
def gaussian_blur(img, kernel_size):
    '''Applies a Gaussian Noise Kernel'''  # 高斯模糊,平滑处理
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)
def directional_gradient(img,direction='x',thresh=[0,255]):
    '''
    使用Opencv Sobel算子来求方向梯度
    img:Grayscale
    direction:x or y axis
    thresh:apply threshold on pixel intensity of gradient image
    output is binary image
    '''
    if direction=='x':
        sobel = cv2.Sobel(img,cv2.CV_64F,1,0)
    elif direction=='y':
        sobel = cv2.Sobel(img,cv2.CV_64F,0,1)
    sobel_abs = np.absolute(sobel)#absolute value
    scaled_sobel = np.uint8(sobel_abs*255/np.max(sobel_abs))
    binary_output = np.zeros_like(sobel)
    binary_output[(scaled_sobel>=thresh[0])&(scaled_sobel<=thresh[1])] = 1
    return binary_output
def region_of_interest(img, vertices):
    '''
    Apply an image mask

    '''
    # define a blank mask to start with
    mask = np.zeros_like(img)

    # defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255

    cv2.fillPoly(mask, vertices, ignore_mask_color)


    masked_image = cv2.bitwise_and(img, mask)  # 与操作
    return masked_image
#转换成鸟瞰图
def birdView(img,M):
    '''
    Transform image to birdeye view
    img:binary image
    M:transformation matrix
    return a wraped image
    '''
    img_sz = (img.shape[1],img.shape[0])
    img_warped = cv2.warpPerspective(img,M,img_sz,flags = cv2.INTER_LINEAR)
    return img_warped
#透视变换(投影变换:为当前成像新换一个投影面)得到变换矩阵
def perspective_transform(src_pts,dst_pts):
    '''
    perspective transform
    args:source and destiantion points
    return M and Minv
    '''
    M = cv2.getPerspectiveTransform(src_pts,dst_pts)
    Minv = cv2.getPerspectiveTransform(dst_pts,src_pts)
    return {'M':M,'Minv':Minv}
#车道像素检测
def find_centroid(image,peak_thresh,window,showMe):
    '''
    find centroid in a window using histogram of hotpixels
    img:binary image
    window with specs {'x0','y0','width','height'}
    (x0,y0) coordinates of bottom-left corner of window
    return x-position of centroid ,peak intensity and hotpixels_cnt in window
    '''
    #crop image to window dimension
    mask_window = image[round(window['y0']-window['height']):round(window['y0']),
                        round(window['x0']):round(window['x0']+window['width'])]
    histogram = np.sum(mask_window,axis=0)
    centroid = np.argmax(histogram)
    hotpixels_cnt = np.sum(histogram)
    peak_intensity = histogram[centroid]
    if peak_intensity<=peak_thresh:
        centroid = int(round(window['x0']+window['width']/2))
        peak_intensity = 0
    else:
        centroid = int(round(centroid+window['x0']))
    if showMe:
        plt.plot(histogram)
        plt.title('Histogram')
        plt.xlabel('horzontal position')
        plt.ylabel('hot pixels count')
        plt.show()
    return (centroid,peak_intensity,hotpixels_cnt)
def find_starter_centroids(image,x0,peak_thresh,showMe):
    '''
    find starter centroids using histogram
    peak_thresh:if peak intensity is below a threshold use histogram on the full height of the image
    returns x-position of centroid and peak intensity
    '''
    window = {'x0':x0,'y0':image.shape[0],'width':image.shape[1]/2,'height':image.shape[0]/2}
    # get centroid
    centroid , peak_intensity,_ = find_centroid(image,peak_thresh,window,showMe)
    if peak_intensity<peak_thresh:
        window['height'] = image.shape[0]
        centroid,peak_intensity,_ = find_centroid(image,peak_thresh,window,showMe)
    return {'centroid':centroid,'intensity':peak_intensity}

if __name__=="__main__":
    img = cv2.imread('test_images/curve_line.jpg')
    imshape = img.shape
    gray_ex = grayscale(img)
    gray_blur = gaussian_blur(gray_ex,3)
    gradx_thresh = [25,255]
    gradx = directional_gradient(gray_blur,direction='x',thresh = gradx_thresh)
    vertices = np.array([[(100,720),(545,470),(755,470),(1290,720)]],dtype=np.int32)
    masked = region_of_interest(gradx,vertices)
    # #开运算去除噪声
    # min_sz = 50
    # cleaned = morphology.remove_small_objects(masked.astype('bool'), min_size=min_sz, connectivity=2)
    src_pts = np.float32([[240, 720], [575, 470], [735, 470], [1200, 720]])
    dst_pts = np.float32([[240, 720], [240, 0], [1200, 0], [1200, 720]])
    transform_matrix = perspective_transform(src_pts, dst_pts)
    warped_image = birdView(masked * 1.0, transform_matrix['M'])
    #车道像素检测
    peak_thresh = 10
    showMe = 0
    centroid_starter_right = find_starter_centroids(warped_image, x0=warped_image.shape[1] / 2,
                                                    peak_thresh=peak_thresh, showMe=showMe)
    centroid_starter_left = find_starter_centroids(warped_image, x0=0, peak_thresh=peak_thresh,
                                                   showMe=showMe)

    display(masked,'masked',color=0)
    display(warped_image, 'BirdViews', color=0)



    # ch_thresh = [50, 255]
    # ch3_hls_binary = color_binary(corr_img, dst_format='HLS', ch=3, ch_thresh=ch_thresh)
    # display(ch3_hls_binary, 'HLS to Binary S', color=0)
    #
    # combined_output = np.zeros_like(gradx)
    # combined_output[((gradx == 1) | (ch3_hls_binary == 1))] = 1
    # display(combined_output, 'Combined output', color=0)
    #
    # mask = np.zeros_like(combined_output)
    # vertices = np.array([[(100, 720), (545, 470), (755, 470), (1290, 720)]], dtype=np.int32)
    # cv2.fillPoly(mask, vertices, 1)
    # masked_image = cv2.bitwise_and(combined_output, mask)
    # display(masked_image, 'Masked', color=0)
    #
    # min_sz = 50
    # cleaned = morphology.remove_small_objects(masked_image.astype('bool'), min_size=min_sz, connectivity=2)
    # display(cleaned, 'cleaned', color=0)


