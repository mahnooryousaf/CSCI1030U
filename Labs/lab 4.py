# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:34:53 2020

@author: Mahnoor
"""

# Part 1
for num in range (101): #using for loop
    if num %2 == 0: #if the number is divisible by 2 within the range
        print(num, end=', ') #print the number
        
        
i = 0 #start at 0
while i <= 101: # numbers from 0- 100
    print(i, end=', ') #print the numbers
    i += 2 #start at zero and increment by 2
    

# Part 2
    midtermMarks = [48.0, 64.25, 71.80, 82.0, 53.45, 59.75, 62.80, 26.5, #created a list with all the marks
55.0, 67.5, 70.25, 52.45, 66.25, 94.0, 65.5, 34.5, 69.25, 52.0]
countf = 0 #defined a variable for each grade range
countd = 0
countc = 0
countb = 0
counta = 0

for i in midtermMarks: #created a loop, so that the program can loop through each of the marks and place them in one of the defined variables
    if i < 50: #for every mark less than 50
        countf += 1 #count how many marks are less than 50
    elif 50 <= i < 60: #for the marks that are between 50-60
        countd += 1 #count the marks from that range
    elif 60 <= i < 70: #if the mark is between 60-70
         countc += 1 #count the marks from that grade range
    elif 70 <= i < 80: #if the mark is from 70-80
        countb += 1 #count how many marks
    else: #any other marks (80+)
        counta += 1 #count them
print("Number of A's:", counta)#prints out the number of As
print("Number of B's:", countb)#prints out the number of Bs
print("Number of C's:", countc)#prints out the number of Cs
print("Number of D's:", countd)#prints out the number of Ds
print("Number of F's:", countf)#prints out the number of Fs