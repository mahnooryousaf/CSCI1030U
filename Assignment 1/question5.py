# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 10:28:01 2018

@author: Mahnoor
"""

def palindromeRec(s):
    if(len(s)<=1):
        return True
    else:
        if(s[0] != s[-1]):
            return False
        else:
            return palindromeRec(s[1:-1])

#Testing
print(palindromeRec('ablewasiereisawelba'))
print(palindromeRec('levelr'))