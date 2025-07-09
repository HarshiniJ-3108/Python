# -*- coding: utf-8 -*-
"""
Created on Thu May 29 14:37:16 2025

@author: harsh
"""

import cv2
import tkinter as tk
root=tk.Tk();
root.title("Image");
root.geometry("500x300")
def read():
    image=cv2.imread("C:\\Users\\harsh\\OneDrive\\Pictures\\Screenshots\\ct.jpg")
    bright_image=50+image
    cv2.imshow('Original Image',image)
    cv2.imshow('Bright Image',bright_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
button=tk.Button(root,text="convert",command=read)
button.pack()