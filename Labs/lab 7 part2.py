# -*- coding: utf-8 -*-
"""
Created on Mon Nov 5 8:34:41 2018

@author: Mahnoor
"""

import random
import matplotlib.pyplot as plt

def insertionSort (num_list):
    for j in range(1,len(num_list)):

        key = num_list[j]
        i = j - 1
        
        while (i > -1 and num_list[i] > key):
            num_list[i + 1] = num_list[i]
            i = i - 1
            
        num_list[i + 1] = key
    
    return(num_list)

def binarySearch (num_list, x ,low, high, counter):
    mid = int((low + high)/2)
    if high >= low:
        counter += 1
        if num_list[mid] == x:
            counter += 1
            return (True, counter)
        
        elif num_list[mid] > x:
            counter += 1
            return binarySearch(num_list, x ,low, mid - 1, counter)
        else:
             counter += 1
             return binarySearch(num_list,x, mid + 1, high, counter)
    else:
        counter += 1
        return (False, counter)


MAXITER = 500   
MINITER = 1
x_array = []
y_array = []
unsort = []

for x in range(MINITER,MAXITER + 1):
    x_array.append(x)
    for y in range(x):
        unsort.append(random.randint(5,109))
    insertionSort(unsort)
    (result,counter) = binarySearch(unsort,random.randint(5,109),0,len(unsort)-1,0)
    print(result, counter,len(unsort))
    y_array.append(counter)
    unsort.clear()
    
print(x_array)
print(y_array)

plt.title("Complexity Graph of Binary Sort")
plt.xlabel("Amount of Elements")
plt.ylabel("Amount of Operations")
plt.plot(x_array,y_array,'g-')