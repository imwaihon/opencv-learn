import numpy as numpy
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg', 0)
# 1 = color(no transparency), 0 = grayscale, 3 = unchanged

cv2.imshow('window name', img) # show image

k = cv2.waitKey(0) # wait indefinitely for a keystroke

if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()


plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()