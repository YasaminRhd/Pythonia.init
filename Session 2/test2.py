import cv2 as cv
import numpy as np

img = cv.imread("photo.jpg")
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

#select the color range and change it to desired color 
light_white = (0, 0, 200)
dark_white = (145, 60, 255)
mask=cv.inRange(hsv,light_white,dark_white)
img[mask>0]=(251,249,13)

#resize the pic
newSize = (img.shape[1]//2, img.shape[0]//2)
img = cv.resize(img, newSize)

cv.imshow("my image", img)
cv.waitKey(0)