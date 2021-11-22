# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 21:05:34 2021

@author: lenovo
"""

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Instantiate three Cat objects using the code provided above.
Cat1 = Cat('Jack', 3)
Cat2 = Cat('Kitti', 2)
Cat3 = Cat('Bella', 10)

# Outside of the class, create a function that finds the oldest cat and returns the cat.
my_cats = {}
my_cats.update({Cat1.name: Cat1.age})
my_cats.update({Cat2.name: Cat2.age})
my_cats.update({Cat3.name: Cat3.age})

def the_oldest(my_cats):
    cat_oldest = -1000000
    for key,value in my_cats.items():
        if value > cat_oldest:
            cat_oldest = value
            cat_name = key
    return cat_name, cat_oldest

cat_name, cat_oldest = the_oldest(my_cats)
print(f'The oldest cat is {cat_name}, and is {cat_oldest} years old.')

        