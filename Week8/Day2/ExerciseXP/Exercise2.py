# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 21:35:23 2021

@author: lenovo
"""

class Dog:
    
    def __init__(self, name, height):
        self.dog_name = name
        self.dog_height = height
        
    def bark(self):
        print(f'{self.dog_name} goes woof!')
    
    def jump(self):
        x = self.dog_height * 2
        print(f'{self.dog_name} jumps {x} cm high!.')
        
davids_dog = Dog('Rex', 50)
print(davids_dog.dog_name)
print(davids_dog.dog_height)
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog('Teacup', 20)
print(sarahs_dog.dog_name)
print(sarahs_dog.dog_height)
sarahs_dog.bark()
sarahs_dog.jump()

if sarahs_dog.dog_height > davids_dog.dog_height:
    print(f'{sarahs_dog.dog_name} is the bigger dog')
else:
    print(f'{davids_dog.dog_name} is the bigger dog')

              
