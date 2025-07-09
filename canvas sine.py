# -*- coding: utf-8 -*-
"""
Created on Sat May 31 11:20:22 2025

@author: harsh
"""

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import numpy as np
root=tk.Tk()
root.title("Matplotlib in Tkinter")
root.geometry("500x600")
def click():
    x=np.linspace(0,10,100)
    y=np.sin(x)
    fig,ax = plt.subplots()
    ax.plot(x,y,"red",marker="*")
    ax.set_title("Sine Wave")
    canvas = FigureCanvasTkAgg(fig,master = root)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH,expand = True)
b1 = tk.Button(root,text = "click",command = click).pack()
root.mainloop()