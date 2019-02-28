#piece wise transformation
import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread('Camera.png',0)
img = np.asarray(img)
pwl = img.copy()
for i in range(len(img)):
    for j in range(len(img[i])):
        if img[i][j]>142 & img[i][j]<250:
            img[i][j]=255;
        else:
            img[i][j]=img[i][j]
cv2.imshow('Result',img)
cv2.imshow('Original',pwl)
cv2.waitKey(100000)
cv2.destroyAllWindows()
plt.show()