# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 10:27:04 2018

@author: Mahnoor
"""

def subset(l1,l2):
#loop through list1
    for i in l1:
#check if i is in list2 and continue
        if i in l2:
            continue
#otherwise return false
else:
return False
return True
#check output of functions
print(subset([1,9,13,15,23], [1,3,5,7,9,11,13,15,17,19,21,23,25])==True)
print(subset([3,8,13,21,25], [1,3,5,7,9,11,13,15,17,19,21,23,25])==False)