import numpy as np
import cv2

def DoNothing(val):
	pass

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

while True:
        counter += 1
        start = cv2.getTickCount()
        #read the image from the camera
        ret, col = cap.read()
        
        frame = cv2.cvtColor(col, cv2.COLOR_BGR2HSV)
        #frame = cv2.blur(frame, (10, 10))
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
        kernel = np.ones((3,3),np.uint8)
        #cv2.imshow('mask_before', thresholded)
        thresholded = cv2.morphologyEx(thresholded, cv2.MORPH_OPEN, kernel)
        #cv2.imshow('mask', thresholded)
        outimage = cv2.bitwise_and(col, col, mask = thresholded)

        countours, hie = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        sorted(countours, key=lambda cnts: cv2.contourArea(cnts))
        try:
                print 'Area: ' + str(cv2.contourArea(countours[-1]))
                cv2.drawContours(outimage, countours[-1], -1, (255, 0, 0))
        except IndexError:
			    pass
        '''
        mom = []
        for cnt in countours:
			    M = cv2.moments(cnt)
			    mom.append(M)
        sorted(mom, key=lambda mm: mm['m00'])
        mom.sort(lambda mm: mm['M00'])
        M = mom[0]
        try:
                cx = int(M['m10']/M['m00'])
                cy = int(M['m01']/M['m00'])
                print (cx, cy)
                cv2.circle(outimage, (cx, cy), 10, (0, 0, 255))
        except ZeroDivisionError:
			    print (-1, -1)
        '''
        #cv2.imshow('original', frame)
        # Display the resulting frame
        cv2.imshow('processed',outimage)
        end = cv2.getTickCount()
        if counter % 10 == 0:
                print "FPS: " + str(1 / ((end - start) / cv2.getTickFrequency()))
        # Quit the program when Q is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

# When everything done, release the capture
print 'closing program'
cap.release()
cv2.destroyAllWindows()
