# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 10:18:27 2021

@author: illouz
"""
#Write code that concatenates two lists together without using the + sign.

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3, 'david', True]

list3 = list1
for x in list2:
    list3.append(x)
print(list3)