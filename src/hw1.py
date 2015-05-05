import cv2




img = cv2.imread('google-icon.png')

val = int(input("input a number: "))

mimg =  img + val

cv2.imshow('origin_image',img)
cv2.imshow('modified_image',mimg)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('new_one.png', img)


