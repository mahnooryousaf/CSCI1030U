# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 16:56:50 2020

@author: Mahnoor
"""
#PART 1
def isPrime(num): #Define function "isPrime"
    for i in range(2, num): #loop through numbers starting from 2 - num
        if num % i == 0: #if the number is divisible by the i value
            return False #then return false
    return True #otherwise return true

def primeFactors(num): #Define function "primeFactors
    lst = [] #create an empty list
    for i in range(2, num): #loop through each number from 2- num 
        if num % i == 0 and isPrime(i): #if the number is divisible by i value and isPrime
            lst.append(i) #then add the number to the list
    return lst #return the list
print(isPrime(8))
print(isPrime(7))
print(primeFactors(187))
print(primeFactors(2058))

#PART 2 
def gregoryLiebniz(numIterations): #define function gregoryLiebniz with argument numIteration
    num = 1
    count = 0 #initizialize the count to 0
    for i in range(0, numIterations): #loop through numbers from 0 - numIterations
        count += num /(2* i + 1) #equations to approximate how many terms to sum and return pi
        num *= -1
        total = 4*count
    
    return total #return the total
  
print(gregoryLiebniz(10000000))

#PART 3 
def jumpMaximum(num): 
    maxNum = 0
    index = 0
    for i in range(len(num)):
        if (maxNum < num[i]):
            maxNum = num[i]
            index = i
    num[index] = num[0]
    num[0] = maxNum
    return num

print(jumpMaximum([1, 2, 3, 4]))
print(jumpMaximum([5, 8, 3, 21, 7, 4, 14]))









