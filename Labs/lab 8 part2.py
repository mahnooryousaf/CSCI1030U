# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 21:19:29 2018

@author: Mahnoor
"""

def insertionSort (arr):
  counter = 0
  for i in range(1, len(arr)):
    key = arr[i]

    j = i - 1
    while j >= 0 and key < arr [j]:
      counter += 2
      arr[j+1] = arr[j]
      j -= 1
      arr[j+1] = key
      return counter

      x_arr = []
      y_arr = []
      unsorted = []
      for x in range(8,1000):
        x_arr.append(x)
       for y in range (x)
          unsorted.append(random.randint(1, 101))
          print (unsorted)
          counter = insertionSort (unsorted)
          unsorted.clear();

    plt.title ("Number of operations in Insertion sort")
    plt.xlabel ("Number of elements")
    plt.ylabel ("Number of operations")
    plt.plot (x_arr, y_arr, 'r-')
