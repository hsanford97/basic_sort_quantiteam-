# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 12:34:52 2017

@author: henry
"""
def recurve(n):
    if n <= 1:
        return 1
    else:
        return n*recurve(n-1)
    
def fall(n,r):
    return(recurve(n)/recurve(n+r-1))

def prob(n,r,total):
    return(fall(n,r)/total**1)

print(prob(365,1,365))
    