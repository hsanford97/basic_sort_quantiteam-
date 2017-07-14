# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 19:32:35 2017

@author: henry
"""
data = open("data.py", 'r')
datalist = []
for i in data:
    if i == "# -*- coding: utf-8 -*-\n":
        pass
    datalist.append(i.split(","))
print(datalist[1])