# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 20:57:10 2021

@author: lenovo
"""
import math

class Circle:
    
    def __init__(self,radius = 1.0):
        self.radius = radius
    
    def perimeter(self):
        return 2*self.radius*math.pi
    
    def area(self):
        return self.radius * self.radius * math.pi
    
    def circle_definition(self):
        print(Circle.perimeter(self))
        print(Circle.area(self))

Example = Circle(25)
Example.circle_definition()
