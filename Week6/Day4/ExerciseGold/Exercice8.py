# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 19:44:51 2021

@author: illouz
"""
import random

user_value = input("please input a number from 1 to 9 (including): ")
while (not(user_value.isdigit())):
    user_value = input("please input a number from 1 to 9 (including): a")
user_value = int(user_value)

random_number = random.randint(1,9)

if user_value == random_number:
    print("WINNER")
else:
    print("better luck next time")

