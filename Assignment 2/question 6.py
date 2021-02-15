# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 05:55:04 2018

@author: Mahnoor
"""

def jumpMaximum(aList):
    aMax = aList[0]
    maxIndex = 0
    for i in range (len(aList)):
        if aMax < aList[i]:
            aMax = aList[i]
            maxIndex = i 
    if maxIndex != 0:
        temp = aList [0]
        aList[0] = aMax
        aMax = temp
        return aList
    
    print(jumpMaximum([5,8,3,21,7,4,14]))
                