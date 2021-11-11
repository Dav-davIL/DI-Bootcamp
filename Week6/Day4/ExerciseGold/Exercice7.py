# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:41:39 2021

@author: illouz
"""

user_value = input("Please enter comma seprated numbers:  ")
my_list = user_value.split(',')
my_tuple = tuple(my_list)

print("List: ", my_list)
print("tuple: ",my_tuple)
