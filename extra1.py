# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 21:50:03 2017

@author: henry
"""

t = "2:01.2"
def time(a):
    timelist = []
    a.split(":")
    for i in a.split(":"):
        timelist.append(i)
    for j in timelist[1].split("."):
        timelist.append(j)
    timelist.pop(1)
    return(timelist)
 
def calc_str2sec(b):
    timelist = time(b)
    if len(timelist)==3:
        return((float(timelist[0])*60)+(float(timelist[1])+float(timelist[2])*(1/10)))
    elif len(timelist)==2:
        return((float(timelist[0])*60)+(float(timelist[1])))
def calc_sec2str(c):
    if c>120:
        value = ["2:"]
        c = c-120
    elif c<120:
        value = ["1:"]
        c = c-60
    
    if c<10:
        value.append("0"+str(c))
    else:
        value.append(str(c))
    return(value[0]+value[1])
        
print(calc_sec2str(calc_str2sec(t)))
        