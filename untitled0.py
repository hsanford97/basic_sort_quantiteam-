# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 23:35:57 2017

@author: henry
"""

def rec(n):
    if n<=1:
        return 1
    else:
        return n*rec(n-1)
  
def choose(n,r):
    return(rec(n)/(rec(r)*rec(n-r)))
#print((choose(90,20)/choose(100,20))+((1-(choose(90,20)/choose(100,20)))*(choose(90,20)/choose(100,20))))
def c(n,r):
    a = 0
    for i in range(n,r):
        a += (.75)**i
    return(a)
print(c(7,11))