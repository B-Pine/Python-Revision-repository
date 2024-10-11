import cv2 as cv
import sys

img = cv.imread("qrImage1.jpg")

if img is None:
    sys.exit("Image not found")

cv.imshow("Image Window", img)
k = cv.waitKey(0)

if k == ord('s'):
    cv.imwrite("img_found.png", img)
