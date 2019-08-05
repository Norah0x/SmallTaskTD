# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 03:10:16 2019

@author: Nora
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Take each frame
im = cv2.imread('./file2.tiff',cv2.IMREAD_GRAYSCALE)

im=cv2.medianBlur(im,5)
im=cv2.medianBlur(im,5)

# Set threshold and maxValue
thresh = 150
maxValue = 200
 
# Basic threshold example
th, dst = cv2.threshold(im, thresh, maxValue, cv2.THRESH_TOZERO_INV)

dst=cv2.fastNlMeansDenoising(dst)

# Display cropped image
cv2.imshow("Image",dst )
cv2.waitKey(0)