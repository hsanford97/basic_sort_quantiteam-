# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 21:46:33 2017

@author: henry
"""
import numpy as np
import matplotlib.pyplot as mlt

def recurve(n):
    if n <= 1:
        return 1
    else:
        return n*recurve(n-1)





num = 20
n = []
n2 = []
np_n = np.array(n)
for i in range(1,num+1):
    
    n.append(recurve(i))
    n2.append(i)
mlt.scatter(n2, n)
mlt.yscale("log")
mlt.show()
