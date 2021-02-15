# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 13:14:57 2020

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
grade = int(input("Enter your mark to know what your letter grade is! " )) #assigned grade to be what the user inputs

if grade < 50: #if the grade is between 0-50 then it prints out F
    print ("F")
elif 50 <= grade < 60 : #if the grade is between 50-60 it prints out D
    print("D")
elif 60 <= grade < 70: #if the grade is between 60-70 it prints out C
    print ("C") 
elif 70 <= grade < 80: #if the grade is between 70-80 it prints out B
    print ("B")
elif 80 <= grade < 100: #if the grade is between 80-100 then it prints out A
    print ("A")
else:
    print ('INVALID INPUT') #if the user enters any other input then it would be invalid
    