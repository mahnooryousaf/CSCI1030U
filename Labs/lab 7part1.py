# -*- coding: utf-8 -*-
"""
Created on Sun Nov 5 8:20:49 2018

@author: Mahnoor
"""

import random


listA = [random.randrange(1, 200, 1) for _ in range(10001)]  #the list of values to be sorted
x = 30
start = 0
end = len(listA)
counter = 0

def binSearch(listA, x, start, end):
    global counter    
    listA.sort() #sorts the list if required 
 
    if start > end: #check base case 
        counter = counter + 1 
        return False 
    
    mid = ((end - start) // 2) + start
 
    # If element is present at the middle itself  
    if listA[mid] == x:
        counter = counter + 1
        return True 
    # If element is smaller than mid, then it  
    # can only be present in left subarray 
    elif x < listA[mid]:
        counter = counter + 1
        return binSearch(listA, x, start, mid - 1)
    else:
        counter = counter + 1
        return binSearch(listA, x, mid + 1, end)

binSearch(listA, x, start, end)
print(binSearch(listA, x, start, end))
print(counter)
