import cv2
import numpy as np

img = cv2.imread('google-icon.png',0)

res_nni = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_NEAREST)
res_bilinear = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_LINEAR)
res_bicubic = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

rows,cols = img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
dst = cv2.warpAffine(img,M,(cols,rows))


cv2.imshow('orgin_image', img)
cv2.imshow('after_nearest-neighbor interpolation', res_nni)
cv2.imshow('after_Bilinear Interpolation', res_bilinear)
cv2.imshow('after_Bicubic Interpolation ', res_bicubic)

cv2.imshow('after_rotation ', dst)



cv2.waitKey(0)
cv2.destroyAllWindows()


