# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:43:37 2018

@author: Mahnoor
"""
list = [1,2,3,4,5]
def sublistInRange(list): #defines the function that takes the list
    min = 2
    max = 5   
    for elements in list:
        if elements < max and elements > min: #if the elements are less than the max and greater then th emin
            list = list(range(min,max))
            return list #the list is returned
        else:
            return False #otherwise the list us changed

sublistInRange(list)
