# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 07:25:11 2021

@author: lenovo
"""

price = 0
person = 0

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}      

for key in family:
    if family[key] >= 3 and family[key] < 12:
        price += 10
        person += 1
    elif family[key] >= 12:
        price += 15
        person += 1

print(person," persons have to pay")
print("price:",price)


            