# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:14:57 2018

@author: Mahnoor
"""

#part 1 
X = 65
if X < 10:
 print("X is small")
elif X < 20:
 print("X is medium")
else:
 print("X is large")
 
 #part 2 
secret = 6 #assigned the secret number to be 6
while True: #used a while look so that the program runs until the user guesses the correct num
    num = int(input("Enter a number:")) #get input from user
    if num == secret: #condition-if you guess the num correct
        print("you got it") 
        break #the program ends if the user guesses the number correct, otherwise the program keeps running
    elif num < secret: 
        print("Higher")
    else:
       print("lower")
       
#part 3
grade = int(input("Enter your mark to know what your letter grade is!"))
if grade > 0 > 50:
    print ("F")
if grade > 50 > 60:
    print("D")
if grade > 60 > 70:
    print ("C")
if grade > 70 > 80:
    print ("B")
if grade > 80 > 100:
    print ("A")
    
