# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 10:33:00 2018

@author: Mahnoor
"""

def isReordering(l1, l2):
    l1.sort()
    l2.sort()
    return l1 == l2


print(isReordering([4, 1, 3, 2], [1, 2, 3, 4]))
print(isReordering([5, 8, 3, 21], [5, 21, 8]))