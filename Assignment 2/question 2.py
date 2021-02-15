# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 07:20:31 2018

@author: Mahnoor
"""

class Product:
    def__init__(self, name, price, weight): #define the function that takes in the name, prince and weight
        self.name = name
        self.price = price
        self.weight = weight
        def getShippingCost(self):
            return self.weight * 10.3 
        def getTax (self):
            return self.price * 0.13 #tax is calculated after the price of the item is inputed 
        def getTotalPrice (self):
            return self.price + self.getTax() + self.getShippingCost() #the toal price of the item is calulated
        
        razor = Product ("Electric Razor", 49, 99, 0.25)
        homeGym = Product ("Home gym", 879.99, 115.0)
        print ("total cost of ", razor.name ":", razor.getTotalPrice())
        print ("total cost of ", homeGym.name ":", homeGym.getTotalPrice())
        