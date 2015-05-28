import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv_logo.png')


# 2D Convolution - Image Filtering 
# LPF - low-pass filters, remove noise/blur image
# HPF - high-pass filters, find edges

kernel = np.ones((5,5),np.float32)/25
# filter kernel, 5x5 window. all pixel within this window are summed and divided by 25

dst = cv2.filter2D(img,-1,kernel)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()

blur = cv2.blur(img,(5,5))
blur = cv2.GaussianBlur(img,(5,5),0)
median = cv2.medianBlur(img,5)
blur = cv2.bilateralFilter(img,9,75,75)