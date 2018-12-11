#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import math
import coordTransform_utils as cu
import numpy
import cv2
level = 17 #下载高德地图的瓦片等级-1
def GeographyToPixel(lng,lat):
    pixelX = (lng+180)/360*math.pow(2,level)*256%256
    pixelY = (2*math.pi - math.log(math.tan(lat*math.pi/180)+1/math.cos(lat*math.pi/180)))/(2*math.pi)*math.pow(2,level)*256%256
    return (pixelX,pixelY)
def GeographyToTile(lng,lat):
    tileX = (lng + 180) / 360 * math.pow(2, level)
    tileY = (1 * math.pi - math.log(math.tan(lat * math.pi / 180) + 1 / math.cos(lat * math.pi / 180))) / (
                2 * math.pi) * math.pow(2, level)
    return (tileX, tileY)
def TileJudge(tileX,tileY):
    if int(tileX) in [110469,110470] and int(tileY) in [48769,48770]:
        return (0,0,110469,48769)
    if int(tileX) in [110471, 110472] and int(tileY) in [48769, 48770]:
        return (1,0,110471,48769)
    if int(tileX) in [110469, 110470] and int(tileY) in [48771, 48772]:
        return (0,1,110469, 48771)
    if int(tileX) in [110471, 110472] and int(tileY) in [48771, 48772]:
        return (1,1,110471, 48771)
    return (0,0,0,0)

if __name__ == '__main__':
    bd_lng = 123.426442
    bd_lat = 41.772139 #百度地图坐标系下的宁恩承像坐标,
    (gd_lng,gd_lat) = cu.bd09_to_gcj02(bd_lng,bd_lat)#转换到高德地图坐标系下的坐标,然后进行标记工作
    # (gd_lng,gd_lat) = cu.wgs84_to_gcj02(gps_lng, gps_lat)#将gps设备获取的地理坐标转换为gd坐标系下
    # print (gd_lng,gd_lat)
    # 使用opencv进行标注:在20个瓦片合成的大图上标记，这样显得太大了，在gui上不方便显示
    # (tileX_init,tileY_init) = (110469,48769)#左上角的瓦片坐标，共横向5纵向4
    # (tileX,tileY) = GeographyToTile(gd_lng,gd_lat)#获取瓦片坐标
    # (pixelX_init,pixelY_init) = GeographyToPixel(gd_lng,gd_lat)
    # (pixelX,pixelY) = (pixelX_init+(int(tileX) - tileX_init)*256,pixelY_init + (int(tileY)-tileY_init)*256)#计算出在大图上的像素坐标
    # img = cv2.imread("../neu_whole/L18/neu.png")
    # cv2.circle(img,(int(round(pixelX)),int(round(pixelY))),10,(0,0,255),-1)
    # cv2.imshow("image",img)
    # cv2.waitKey(0)
    #使用opencv进行标注：把16个瓦片分为4部分。第一部分的瓦片坐标：（69,69）,(70,69),(69,70),(70,70);第二部分：...
    (tileX, tileY) = GeographyToTile(gd_lng, gd_lat)  # 获取瓦片坐标
    print (int(tileX),int(tileY))
    (pixelX_init, pixelY_init) = GeographyToPixel(gd_lng, gd_lat)#获取像素坐标
    print (pixelX_init,pixelY_init)
    (numX,numY,tileX_init,tileY_init) = TileJudge(tileX,tileY)#判断瓦片落在哪一个部分,返回这个部分的左上角的瓦片坐标
    print (numX,numY,tileX_init,tileY_init)
    (pixelX,pixelY) = (pixelX_init+(int(tileX) - tileX_init)*256,pixelY_init + (int(tileY)-tileY_init)*256)#计算在该部分瓦片的像素坐标
    print(pixelX,pixelY)
    img = cv2.imread("../neu_tiles/"+str(numX)+"_"+str(numY)+"/tile_png/L18/neu.png")
    cv2.circle(img,(int(round(pixelX)),int(round(pixelY))),10,(0,0,255),-1)
    cv2.imshow("image",img)
    cv2.waitKey(0)
