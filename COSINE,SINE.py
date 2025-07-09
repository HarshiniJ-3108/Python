# -*- coding: utf-8 -*-
"""
Created on Mon May 26 12:07:47 2025

@author: harsh
"""

a= 0
b = 1
print("Fibonacci sequence:")
for i in range(10):
    print(a,b)
    a, b = b, a + b
    
n_terms = int(input("Enter the number of terms: "))
a, b = 0, 1

print("Fibonacci sequence:")
for i in range(n_terms):
    print(a)
    a, b = b, a + b
    
