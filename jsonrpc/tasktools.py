import cv2
import subprocess
import time
#from imutils.video.pivideostream import PiVideoStream

def thread_open(cmd):
    subprocess.Popen(cmd)
    while True:
        time.sleep(1)


def buildModel(cfg):
    img = cv2.imread("model.jpg")

    crop_img = img[cfg.model_roi[1]:cfg.model_roi[1] + cfg.model_roi[3], cfg.model_roi[0]:cfg.model_roi[0] + cfg.model_roi[2]]
    filename = cfg.models[-1]
    cv2.imwrite(filename, crop_img)