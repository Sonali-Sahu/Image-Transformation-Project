#powr law transformation
import cv2
import numpy as np
img_1=cv2.imread('Camera.png',0)
gamma=2
img_2=np.power(img_1,gamma)
cv2.imshow('input image',img_1)
cv2.imshow('gamma image',img_2)
cv2.waitKey(100000)
cv2.destroyAllWindows()