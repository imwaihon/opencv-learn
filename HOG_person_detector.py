import cv2
import numpy as np

# Helper functions

def inside(r, q):
    rx, ry, rw, rh = r
    qx, qy, qw, qh = q
    return rx > qx and ry > qy and rx + rw < qx + qw and ry + rh < qy + qh

def draw_detections(img, rects, thickness = 1):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        pad_w, pad_h = int(0.15*w), int(0.05*h)
        cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)



# Load video
cap = cv2.VideoCapture('testcam.mov')

# Set up HOG
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:

    ret, frame = cap.read()

    # Resize frame
    frame = cv2.resize(frame, (400, 400), interpolation = cv2.INTER_AREA)

    found, w = hog.detectMultiScale(frame, winStride=(8,8), padding=(32,32), scale=1.05)
    found_filtered = []

    for ri, r in enumerate(found):
        for qi, q in enumerate(found):
            if ri != qi and inside(r, q):
                break
        else:
            found_filtered.append(r)

    draw_detections(frame, found)
    draw_detections(frame, found_filtered, 3)

    cv2.imshow('Detection View', frame)

    # Break if ESC
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break

# Release video from memory     
cap.release()
cv2.destroyAllWindows()

