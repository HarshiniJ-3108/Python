# -*- coding: utf-8 -*-
"""
Created on Thu May 29 14:45:11 2025

@author: harsh
"""

import tkinter as tk
window=tk.Tk();
window.title("My app");
window.geometry("600x600");
def add():
    value1= int(value1entry.get());
    value2= int(value2entry.get());
    result = value1 + value2;
    f.config(text=f"the output is {result}")
def sub():
    value1=int(value1entry.get());
    value2=int(value2entry.get());
    result = value1-value2;
    f.config(text=f"the output is {result}")  
def mul():
    value1=int(value1entry.get());
    value2=int(value2entry.get());
    result = value1*value2;
    f.config(text=f"the output is {result}")  
def div():
    value1=int(value1entry.get());
    value2=int(value2entry.get());
    result = value1/value2;
    f.config(text=f"the output is {result}")    
value1 = tk.Label(window,text="value1");
value1.grid(row=0,column=0);
value1entry=tk.Entry(window);
value1entry.grid(row=0,column=1);

value2=tk.Label(window,text="value2");
value2.grid(row=1,column=0);
value2entry=tk.Entry(window);
value2entry.grid(row=1,column=1);

output=tk.Label(window,text="output");
output.grid(row=2,column=0);
f=tk.Label(window);
f.grid(row=2,column=1);

button=tk.Button(window,text="+",command=add);
button.grid(row=3,column=0);
button=tk.Button(window,text="-",command=sub);
button.grid(row=3,column=1);
button=tk.Button(window,text="*",command=mul);
button.grid(row=4,column=0);
button=tk.Button(window,text="/",command=div);
button.grid(row=4,column=1);
input("wait for key press")
