# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 00:58:48 2019

@author: Nora
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('./file2.tiff',cv2.IMREAD_GRAYSCALE)
img=cv2.medianBlur(img,5)

img=cv2.medianBlur(img,5)

im_color = cv2.applyColorMap(img, cv2.COLORMAP_HOT	)

cv2.imshow('nan',im_color)

cv2.waitKey()
