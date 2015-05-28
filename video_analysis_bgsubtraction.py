import numpy as np
import cv2

MIN_AREA = 800
firstFrame = None

cap = cv2.VideoCapture('testcam.mov')

fgbg = cv2.BackgroundSubtractorMOG()

def nothing():
	pass

while(1):

	ret, frame = cap.read()

	frame = cv2.resize(frame, (400, 400), interpolation = cv2.INTER_AREA)
	fgmask = fgbg.apply(frame)

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)
 
	# if the first frame is None, initialize it
	if firstFrame is None:
		firstFrame = gray
		continue

	# compute the absolute difference between the current frame and
	# first frame
	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 30, 255, cv2.THRESH_BINARY)[1]
 
	# dilate the thresholded image to fill in holes, then find contours
	# on thresholded image
	thresh = cv2.dilate(thresh, None, iterations=2)
	(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
 
	# loop over the contours
	for c in cnts:
		# if the contour is too small, ignore it
		if cv2.contourArea(c) < MIN_AREA:
			continue
 
		# compute the bounding box for the contour, draw it on the frame,
		# and update the text
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)



	cv2.imshow('original', frame)
	cv2.imshow('mask',fgmask)

	k = cv2.waitKey(100) & 0xff
	if k == 27:
	    break

cap.release()
cv2.destroyAllWindows()

