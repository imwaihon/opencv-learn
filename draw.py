import numpy as np
import cv2

# Create a black image
black_img = np.zeroes((512,512,3), np.uint8)

# Diagnoal blue line with thickness of 5px
diag_blue_line = cv2.line(img, (0,0), (511,511),(255,0,0), 5)

rect = cv2.rectangle(img, (384,0), (510,128), (0,255,0), 3)

circle = cv2.circle(img, (447,63), 63, (0,0,255), -1)

ellipse = cv2.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# POLYGON

# Create array of points as vertices
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img,[pts],True,(0,255,255))

'''

If third argument is False, you will get a polylines joining all the points, not a closed shape.

cv2.polylines() can be used to draw multiple lines. Just create a list of all the lines you want 
to draw and pass it to the function. All lines will be drawn individually. It is more better and faster way 
to draw a group of lines than calling cv2.line() for each line.

'''

# Text

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

