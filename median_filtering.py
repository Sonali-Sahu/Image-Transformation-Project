#median_filtering
#imports
import numpy as np
import cv2
import matplotlib.pyplot as plt

# load in image and add Salt and pepper noise
moon = cv2.imread('Camera.png', 0)

######################################################## ADD SALT & PEPPER NOISE
# salt and peppering manually (randomly assign coords as either white or black)
rows, cols = moon.shape
salt_vs_pepper_ratio = 0.9
amount = 0.1
moon_salted_and_peppered = moon.copy()
num_salt = np.ceil(amount * moon.size * salt_vs_pepper_ratio)
coords = [np.random.randint(0, i - 1, int(num_salt)) for i in moon.shape]
moon_salted_and_peppered[coords] = 255
num_pepper = np.ceil(amount * moon.size * (1 - salt_vs_pepper_ratio))
coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in moon.shape]
moon_salted_and_peppered[coords] = 0

############################################ APPLY MEDIAN FILTER TO REMOVE NOISE
# The second argument is the aperture linear size; it must be odd and greater
# than 1, for example: 3, 5, 7
moon_median = cv2.medianBlur(moon, 3)

# show all three images using opencv
cv2.imshow("Salted and peppered",moon_salted_and_peppered)
cv2.imshow("remove salt and peppered",moon_median)
cv2.waitKey(100000)
cv2.destroyAllWindows()


