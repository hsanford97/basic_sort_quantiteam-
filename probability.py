# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 15:58:08 2017

@author: henry
"""
n = 50
def fact(n):
    if n <= 1:
        return 1
    else:
        return n*fact(n-1)
def choose(n,r):
    return fact(n)/(fact(r)*fact(n-r))
print(5/7)