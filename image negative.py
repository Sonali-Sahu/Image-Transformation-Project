#image negative
import cv2
img_1=cv2.imread('Camera.png',0)
img_2=255-img_1
cv2.imshow('input image',img_1)
cv2.imshow('image negative',img_2)
cv2.waitKey(100000)
cv2.destroyAllWindows()