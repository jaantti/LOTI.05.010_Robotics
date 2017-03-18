import numpy as np
import cv2

img = cv2.imread('img2.jpg')
gray = cv2.imread('img2.jpg', 0)

ret, thresh = cv2.threshold(gray, 127, 255, 1)

contours, h = cv2.findContours(thresh, 1, 2)
cv2.putText(gray, 'text', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, 0)

for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True)
    print len(approx)
    brect = cv2.boundingRect(cnt)
    print brect[:2]
    cv2.putText(gray, str(len(approx)), brect[:2], cv2.FONT_HERSHEY_SIMPLEX, 1, 0)
    if len(approx) == 5:
        print "pentagon"
        cv2.drawContours(img, [cnt], 0, 255, -1)
    elif len(approx) == 3:
        print "triangle"
        cv2.drawContours(img, [cnt], 0, (0, 255, 0), -1)
    elif len(approx) == 4:
        print "square"
        cv2.drawContours(img, [cnt], 0, (0, 0, 255), -1)
    elif len(approx) == 9:
        print "half-circle"
        cv2.drawContours(img, [cnt], 0, (255, 255, 0), -1)
    elif len(approx) > 15:
        print "circle"
        cv2.drawContours(img, [cnt], 0, (0, 255, 255), -1)

cv2.imshow('img', img)
cv2.imshow('img2', gray)
cv2.imwrite('img gray.png', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
