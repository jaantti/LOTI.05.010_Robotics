import numpy as np
import cv2

def DoNothing(val):
        pass

# open the camera
cap = cv2.VideoCapture(0)
val1 = 0
val2 = 255
cv2.namedWindow('processed')
cv2.createTrackbar('hMin', 'processed', val1, 255, DoNothing)
cv2.createTrackbar('hMax', 'processed', val2, 255, DoNothing)

while True:
        #read the image from the camera
        ret, orig = cap.read()        
        frame = cv2.cvtColor(orig, cv2.COLOR_BGR2HSV)
        # color detection limits
        lB = cv2.getTrackbarPos('hMin', 'processed')
        lG = 0
        lR = 0
        hB = cv2.getTrackbarPos('hMax', 'processed')
        hG = 255
        hR = 255
        lowerLimits = np.array([lB, lG, lR])
        upperLimits = np.array([hB, hG, hR])

        # Our operations on the frame come here
        thresholded = cv2.inRange(frame, lowerLimits, upperLimits)
        outimage = cv2.bitwise_and(orig, orig, mask = thresholded)


        cv2.imshow('original', orig)
        # Display the resulting frame
        cv2.imshow('processed',outimage)
        # Quit the program when Q is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

# When everything done, release the capture
print 'closing program'
cap.release()
cv2.destroyAllWindows()
