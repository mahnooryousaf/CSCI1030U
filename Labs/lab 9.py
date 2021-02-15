# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 13:30:40 2018

@author: Mahnoor
"""


class Shape:
    def getArea(self): 
        return 0
        
    def getPerimeter(self): 
        return 0
              
class Rectangle(Shape):
    
    def __init__ (self, width, height): 
        self.width = width 
        self.height = height 
        
    def getArea(self): 
        self.area = self.width*self.height 
        return self.area
        
    def getPerimeter(self): 
        self.perimeter = (self.width*2) + (self.height*2)
        return self.perimeter

''' 
this  class is for the area and perimeter of a circle
returns the area and perimeter of a circle 
'''        

class Circle(): 
    
     def __init__ (self, radius): 
        self.radius = radius
        
     def getArea(self): 
        self.area = 3.14 * self.radius**2 
        return self.area
        
     def getPerimeter(self): 
        self.perimeter = (2*3.14) * self.radius
        return self.perimeter
    
        
#initiates the rectangle      
rectangle1 = Rectangle(2,2)
#gets the area for the rectangle
area = rectangle1.getArea() 
#gets the perimeter for the rectangle
perimeter = rectangle1.getPerimeter() 
print('The area of rectangle1 =', area, 'The perimeter of rectangle1 =', perimeter) 
print()
#initiates the circle
circle1 = Circle(10) 
#gets the area for the circle
area = circle1.getArea()
#gets the perimeter for the circle
perimeter = circle1.getPerimeter() 
print('The area of circle1 =', area, 'The perimeter of circle1 =', perimeter)