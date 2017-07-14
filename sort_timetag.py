# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 23:29:51 2017

@author: henry
"""
num_list = [["henry", 100], ["ian", 110], ["marc", 90], ["sean", 120], ["george", 95]]
num2_list = [100,110,90,120,95]
#sort, tag = dist 
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
sort(num_list, compare_func_name)
for value in reversed(num_list):
    print(value)
