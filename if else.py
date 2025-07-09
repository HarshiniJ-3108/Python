# -*- coding: utf-8 -*-
"""
Created on Thu May 29 14:47:14 2025

@author: harsh
"""


import cv2
import tkinter as tk
root = tk.Tk()
root.title("Image")
root.geometry("500x300")
def read():
    image = cv2.imread("C:\\Users\\harsh\\OneDrive\\Pictures\\Screenshots\\ct.jpg",0)
    if image is None:
        print("Error:Image not loaded")
    else:
        new_image=image   
        for row in range(image.shape[0]):          
            for col in range(image.shape[1]):
                if value > 150:
                    brightened[row,col]=min(value+50,255)
    cv2.imshow("original image")
    cv2.imshow('Brightened Image',brightened)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
button = tk.Button(root, text="convert", command=read)
button.pack()

import cv2
import tkinter as tk
root=tk.Tk();
root.title("Image");
root.geometry("500x300")
def read():
    image=cv2.imread("C:\\Users\\harsh\\OneDrive\\Pictures\\Screenshots\\ct.jpg",0)
    if image is None:
        print("Error:Image not loaded")
    else:
        new_image=image   
        for row in range(image.shape[0]):
            for col in range(image.shape[1]):
                value=image[row,col]
                if value > 150:
                    new_image[row,col]=min(value+50,255)    
        cv2.imshow('Original Image',image)
        cv2.imshow('New Image',new_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
button=tk.Button(root,text="Convert",foreground="orange",background="purple",command=read).pack();
