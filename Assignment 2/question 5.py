# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 10:28:01 2018

@author: Mahnoor
"""

def palindromeRec(s): #defines a recursive function that takes a string as a palindrome
    if(len(s)<=1):  
        return True #return true if the string is a palindrome 
    else:
        if(s[0] != s[-1]): #if the elements are not equal when reversed then return false
            return False 
        else:
            return palindromeRec(s[1:-1])

#Testing
print(palindromeRec('level')) #prints true because it is a palindrome
print(palindromeRec('lever')) #prints false