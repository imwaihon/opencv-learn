import cv2
import numpy as np

img = cv2.imread('j.png',0)

# Erosion

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)

# Dilation
dilation = cv2.dilate(img,kernel,iterations = 1)

# Opening -> Erode then Dilate
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# Closing
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Morphology Gradient opening - closing
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
# Tophat opening - input
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
# Blackhat closing - input
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


