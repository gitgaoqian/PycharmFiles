import cv2
import numpy as np
import cv2.cv as cv
cap = cv2.VideoCapture(-2)

# Define the codec and create VideoWriter object
fourcc = cv2.cv.FOURCC(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20, (640, 480))

while(1):
    # get a frame
    ret, frame = cap.read()
    # save a frame
    out.write(frame)
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()











# import cv2
#
# cam = cv2.VideoCapture(-1)
# img_counter = 0
# while cam.isOpened():
#     ret, frame = cam.read()
#     cv2.imshow("test", frame)
#     if not ret:
#         break
#     key = cv2.waitKey(1) & 0xFF
#
#     if key == 27:
#         # press ESC to escape (ESC ASCII value: 27)
#         print("Escape hit, closing...")
#         break
#     elif key == 32:
#         # press Space to capture image (Space ASCII value: 32)
#         img_name = "opencv_frame_{}.png".format(img_counter)
#         cv2.imwrite(img_name, frame)
#         print("{} written!".format(img_name))
#         img_counter += 1
#     else:
#         pass
# cam.release()
# cv2.destroyAllWindows()
