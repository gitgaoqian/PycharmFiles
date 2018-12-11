import cv2
import numpy as np
import cv2.cv as cv

import cv2
img = cv2.imread("E://Pictures//0330m.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
rect = cv2.minAreaRect(cnt)
box = cv2.cv.BoxPoints(rect) # cv2.boxPoints(rect) for OpenCV 3.x
box = np.int0(box)
cv2.drawContours(img, [box], 0, (0, 0, 255), 2)
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)



cv2.namedWindow("Contours", cv2.WINDOW_NORMAL)
cv2.imshow("Contours", img)


cv2.waitKey(0)
cv2.destroyAllWindows()