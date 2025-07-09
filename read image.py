# -*- coding: utf-8 -*-
"""
Created on Thu May 29 14:31:18 2025

@author: harsh
"""

import cv2
imgpath = "C:\\Users\\harsh\\OneDrive\\Pictures\\Screenshots\\ct.jpg"
img = cv2.imread(imgpath,0)
cv2.imshow('fig 1',img)
cv2.waitKey()
cv2.destroyAllWindows()