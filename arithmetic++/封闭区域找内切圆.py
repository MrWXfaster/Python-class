# -*- coding: utf-8 -*-
import cv2
import cv2.cv2 as cv
import numpy as np

image=cv2.imread('/home/asus/PycharmProjects/Python class/arithmetic++/Figure_1.png')
image_bin=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)

retval,image_bin=cv2.threshold(image_bin,245,255,cv2.THRESH_BINARY_INV)


contours, hierarchy = cv2.findContours(image_bin.copy(),cv2.RETR_CCOMP , cv2.CHAIN_APPROX_SIMPLE)
#print(len(contours))
#

# cv2.drawContours(image_bin, contours, -1, (0, 0, 255), 3)
# cv2.namedWindow("img",0)
# cv2.imshow("img", image_bin)
# cv2.waitKey(0)

image_with_contour=np.zeros(image.shape, np.uint8)
dist=np.zeros((image.shape[0],image.shape[1]))
#
cv2.drawContours(image_with_contour,contours,-1,(255,255,255),1)
#
for ind_y in range(image.shape[0]):
    for ind_x in range(image.shape[1]):
        dist[ind_y,ind_x] = cv2.pointPolygonTest(contours[0],(ind_y,ind_x),True)
#
minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(dist)
print(maxVal, minLoc, maxLoc)
cv2.circle(image,(maxLoc[1],maxLoc[0]),int(maxVal),(0, 255, 0),-1)

cv2.imshow('original', image)
cv2.imshow('contour', image_with_contour)

cv2.waitKey(0)
cv2.destroyAllWindows()
