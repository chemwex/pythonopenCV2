# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 12:30:40 2024

@author: Geoffrey Chemwa
"""

import cv2

#cv2.imread('lena.jpg',0)
imgray = cv2.imread('lena.jpg',0) #read image color in grayscale.
print(imgray)
imgcolor = cv2.imread('lena.jpg',1) #read image file in color.
print(imgcolor)
imgasis = cv2.imread('lena.jpg',-1) #read image file as is.
print(imgasis)

cv2.imshow('imagegray',imgray)   #show the image in a window whose title is imagegray
cv2.imshow('imagecolor',imgcolor)   #show the image in a window whose title is imagecolor
cv2.imshow('imageasis',imgasis)   #show the image in a window whose title is imageasis   
cv2.waitKey(5000)         #show the window for 5 seconds on the screen
cv2.destroyAllWindows()   #destroy the created window
