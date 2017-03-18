import numpy as np
import cv2


def DoNothing(val):
    pass

def biggestBlob(conts):
    maxArea = 0
    bestCont = None
    for cnt in conts:
        area = cv2.contourArea(cnt)
        if area > maxArea:
            maxArea = area
            bestCont = cnt
    return bestCont
# open the camera
cap = cv2.VideoCapture(0)
counter = 0

hmin = 0
hmax = 179

smin = 0
smax = 255
vmin = 0
vmax = 255

cv2.namedWindow('processed')
cv2.createTrackbar('hMin', 'processed', hmin, 179, DoNothing)
cv2.createTrackbar('hMax', 'processed', hmax, 179, DoNothing)
cv2.createTrackbar('sMin', 'processed', smin, 255, DoNothing)
cv2.createTrackbar('sMax', 'processed', smax, 255, DoNothing)
cv2.createTrackbar('vMin', 'processed', vmin, 255, DoNothing)
cv2.createTrackbar('vMax', 'processed', vmax, 255, DoNothing)

params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.minArea = 20

while True:
    counter += 1
    #read the image from the camera
    ret, col = cap.read()

    frame = cv2.cvtColor(col, cv2.COLOR_BGR2HSV)
    #frame = cv2.GaussianBlur(frame, (5, 5), 1)
    # color detection limits
    lH = cv2.getTrackbarPos('hMin', 'processed')
    lS = cv2.getTrackbarPos('sMin', 'processed')
    lV = cv2.getTrackbarPos('vMin', 'processed')
    hH = cv2.getTrackbarPos('hMax', 'processed')
    hS = cv2.getTrackbarPos('sMax', 'processed')
    hV = cv2.getTrackbarPos('vMax', 'processed')
    lowerLimits = np.array([lH, lS, lV])
    upperLimits = np.array([hH, hS, hV])

    # Our operations on the frame come here
    thresholded = cv2.inRange(frame, lowerLimits, upperLimits)
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    thresholded = cv2.morphologyEx(thresholded, cv2.MORPH_ERODE, kernel)
    conts, hie = cv2.findContours(thresholded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    biggest = biggestBlob(conts)
    m = cv2.moments(biggest)
    cx, cy = int(m['m10']/m['m00']), int(m['m01']/m['m00'])

    outimage = cv2.bitwise_and(col, col, mask=thresholded)
    cv2.drawContours(outimage, [biggest], -1, (0, 255, 0), 3)
    cv2.circle(outimage, (cx, cy), 10, (0, 0, 255), thickness=3)

    cv2.imshow('processed', outimage)
    end = cv2.getTickCount()
    if counter % 10 == 0:
        pass
    # Quit the program when Q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
print 'closing program'
cap.release()
cv2.destroyAllWindows()