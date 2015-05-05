import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('google-icon.png',0)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))
cv2.imshow('verse', res)

hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.hist(img.ravel(),256,[0,256])
plt.title('before Histogram for gray scale picture')
plt.show()


hist = cv2.calcHist([equ],[0],None,[256],[0,256])
plt.hist(equ.ravel(),256,[0,256])
plt.title('after Histogram for gray scale picture')
plt.show()




# color = ('b','g','r')

# for channel,col in enumerate(color):
# 	histr = cv2.calcHist([img], [channel], None, [256], [0,256])
# 	plt.plot(histr, color = col)
# 	plt.xlim([0,256])
# plt.title('Histogram table')
# plt.show()






cv2.waitKey(0)
cv2.destroyAllWindows()