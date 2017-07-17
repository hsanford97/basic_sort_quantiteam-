# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 22:54:08 2017

@author: henry
"""
import numpy as np
import matplotlib.pyplot as mlt

#sorting for quantiteam 
#tags with list = dist/time

#test variables. These are general forms of the input data. 
num_list = [["henry", 100], ["ian", 110], ["marc", 90], ["sean", 120], ["george", 95]]
num2_list = [100,110,90,120,95]

#componantes of the sort function, based on distance 
def compare_func_name(a,b):
    return a[1]<=b[1]
def compare_func(a,b):
    return a<=b
def swap(the_list, c,d):
    temp = the_list[c]
    the_list[c] = the_list[d]
    the_list[d] = temp
    
def partition(the_list, p, r, compare_func):
    pivot = the_list[r]
    i = p-1
    j = p
    
    #mechanics 
    while j <= r-1:
        if compare_func(the_list[j], pivot):
            i+= 1
            swap(the_list, i, j)
            j += 1
        else:
            j += 1
    swap(the_list, r, i+1)
    
    return i
            
def quicksort(the_list, p, r, compare_func):
    
    if p<r:
        
        q = partition(the_list, p, r, compare_func)
        quicksort(the_list, p, q, compare_func)
        quicksort(the_list, q+1, r, compare_func)
def sort(the_list, compare_func):
    quicksort(the_list, 0, len(the_list)-1, compare_func)

#main function, this is a test function for now, but calls the sort functions and produces a graph, ordered list, and avg,max,min
def main(num_list, compare_func_name):
    sort(num_list, compare_func_name)
    new_list = []
    name_list = []
    index_list = []
    extra = 0

    for value in num_list:
        
        new_list.append(value[1])
        name_list.append(value[0])
        index_list.append(extra)
        extra +=1 
    
    #creates a graph
    mlt.bar(index_list, new_list)
    mlt.title("Avg = "+str(np.average(new_list))+" Max = "+str(np.max(new_list)))
    mlt.xlabel("athlete")
    mlt.ylabel("score")
    mlt.xticks(index_list, name_list)
    mlt.show()
    
    
    #in the future, this should return a sorted list, and the avg,max,min from the list
    return [np.average(new_list), np.max(new_list), np.min(new_list)]
print(main(num_list, compare_func_name)[1])

#print(num_list)
