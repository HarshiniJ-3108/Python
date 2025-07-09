# -*- coding: utf-8 -*-
"""
Created on Thu May 29 15:41:09 2025

@author: harsh
"""
import numpy as np

a = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])
row=a.shape[0]
column=a.shape[1]
for i in range(row):                
    for j in range(column):
        a[i][j] += 1 
print(a)
input("wait for key press")
