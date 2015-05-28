import cv2
import numpy as np

img = cv2.imread('messi5.jpg')

# Scaling

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

#OR

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

'''

Different interpolation methods are used. Preferable interpolation methods 
are cv2.INTER_AREA for shrinking and cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR 
for zooming. By default, interpolation method used is cv2.INTER_LINEAR for all 
resizing purposes.

'''


# Translation

rows.cols = img.shape

M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))
# (cols,rows) is for (width, height)

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Rotation
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))

# Affine Transformation

# Perspective Transformation