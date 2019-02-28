#histogram equalisation
import cv2
import matplotlib.pyplot as plt
img = cv2.imread('Camera.png',0) #The ',0' makes it read the image as a grayscale image
row, col = img.shape[:2]

# to make a histogram (count distribution frequency)
def df(img):  
    values = [0]*256
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            values[img[i,j]]+=1
    return values
# cumulative distribution frequency

def cdf(hist):  
    cdf = [0] * len(hist)   
    cdf[0] = hist[0]
    for i in range(1, len(hist)):
        cdf[i]= cdf[i-1]+hist[i]
    
    cdf = [ele*255/cdf[-1] for ele in cdf]      
    return cdf

def equalize_image(image):
    my_cdf = cdf(df(img))
    import numpy as np
    image_equalized = np.interp(image, range(0,256), my_cdf)
    return image_equalized

eq = equalize_image(img)
cv2.imwrite('equalized.png', eq)
im=cv2.imread('equalized.png',0)
cv2.imshow('equalized',im)
plt.hist(img.ravel())
cv2.waitKey(100000)
cv2.destroyAllWindows()