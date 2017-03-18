import numpy as np
import cv2

#Location of the image
img = cv2.imread('img.jpg')
gray = cv2.imread('img.jpg', 0)

#Thresholding the image
ret, thresh = cv2.threshold(gray, 127, 255, 1)

#Finding the contours in the image
contours, h = cv2.findContours(thresh, 1, 2)

for cnt in contours:
    #Approximation shapes to polygons
    #Length of approx shows the number of sides of the approximated polygon 
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    #Print the approximation
    print len(approx)
    if len(approx) == 3:
        print "triangle"
        #Paint over the processed shape
        cv2.drawContours(img, [cnt], 0, (255, 0, 0), -1)
    elif len(approx) == 4:
        print "square"
        cv2.drawContours(img, [cnt], 0, (0, 255, 0), -1)

#Show the processed images    
cv2.imshow('img', img)
cv2.imshow('img2', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
