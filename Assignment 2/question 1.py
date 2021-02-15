# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:09:15 2018

@author: Mahnoor
"""

class student:
    def __init__(self,name,s_id): #constructor of the student class which will initilize all the variables.
        #constructor of the student class which will initilize all the variables.
        self.name = name
        self.s_id=s_id
        self.labs = 0
        self.assignments = 0
        self.midterm = 0
        self.final_mark = 0
    def average(self, labs, assignments, midterm, final_mark)
        #average method which will return tot_marks of the student.
        self.labs = labs
        self.assignments = assignments
        self.midterm = midterm * 30/100
        self.final_mark = final_mark * 40/100
        tot_mark = self.labs + self.assignments + self.midterm + self.final_mark
        return tot_mark
    def grade (self,labs,assignments,midterm,final_mark):
        #Grade method which will return grade of the particular student.
#calling average method to get the student marks.
        marks=self.average(labs,assignments,midterm,final_mark)
        if marks>=80 and marks<=100:
        print ("Your grade is::A")
    elif marks>=70 and marks<=79:
        print ("Your grade is::B")
    elif marks>=60 and marks<=69:
        print ("Your grade is::C")
    elif marks>=50 and marks<=59:
        print ("Your grade is::D")
    elif marks>=0 and marks<=49:
        #If student got less than 49 marks then Return 'F' grade.
        print ("Your grade is::F")
        #Creating object of the class.
        s=student("John","s001")
        #calling grade function.
        s.grade(8,18,80,80)
