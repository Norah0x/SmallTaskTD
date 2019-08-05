# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 01:27:00 2019

@author: Nora
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('./file2.tiff')
img=cv2.medianBlur(img,3)
img=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)



MIN = np.array([0,135, 135],np.uint8)
MAX = np.array([35, 255, 255],np.uint8)

kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

img = cv2.inRange(img, 135, 200)

#frame_threshed = cv2.inRange(closing, MIN, MAX)
cv2.imshow('',img )
cv2.waitKey()

#cv2.imwrite('output3.jpg', frame_threshed)
'''

cv2.imshow('',gray_filtered)
cv2.waitKey()


img = cv2.imread('./file2.tiff',0)



#im_color = cv2.applyColorMap(img, cv2.COLORMAP_HOT	)

'''