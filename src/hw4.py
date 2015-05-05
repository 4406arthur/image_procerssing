import cv2
import numpy as np

img = cv2.imread('google-icon.png',0)


scale = 1
delta = 0
ddepth = cv2.CV_16S



grad_x = cv2.Sobel(img,ddepth,1,0,ksize = 3, scale = scale, delta = delta,borderType = cv2.BORDER_DEFAULT)
grad_y = cv2.Sobel(img,ddepth,0,1,ksize = 3, scale = scale, delta = delta, borderType = cv2.BORDER_DEFAULT)


abs_grad_x = cv2.convertScaleAbs(grad_x)   # converting back to uint8
abs_grad_y = cv2.convertScaleAbs(grad_y)

dst = cv2.addWeighted(abs_grad_x,0.5,abs_grad_y,0.5,0)

res = np.hstack((img,dst))

cv2.imshow('Answer',res)
cv2.waitKey(0)


