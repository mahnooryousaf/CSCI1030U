# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 00:36:18 2020

@author: Mahnoor
"""
#PART 1
import math #set up math module
n = int(input("enter a number to estimate pi"))
pi_estimated = n*math.sin(math.radians(180/n)) #the formula for pi
print(pi_estimated) #print the estimate

#PART 2

n = 3 
while abs(pi_estimated - math.pi) >= 0.00000000001: #formula for estimated pi -actual pi value while greater tha or equal to 0.00000000001
    n += 1 #add a side length each iteration until completion of pi
print(pi_estimated, '= pi of a polygon with', n, 'sides')