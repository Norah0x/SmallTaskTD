# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 01:50:50 2019

@author: Nora
"""

# import Numpy 
import numpy as np 
import cv2 
from matplotlib import pyplot as plt


# read a image using imread 
img = cv2.imread('./file2.tiff')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_gray = np.array([100, 50, 150], np.uint8)
upper_gray = np.array([360, 50, 255], np.uint8)
mask_gray = cv2.inRange(hsv, lower_gray, upper_gray)
img_res = cv2.bitwise_and(img, img, mask = mask_gray)
cv2.imshow('',img_res)
cv2.waitKey()