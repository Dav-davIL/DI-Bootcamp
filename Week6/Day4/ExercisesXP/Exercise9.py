# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 06:38:09 2021

@author: lenovo
"""

user_fruits = input("Please enter your favorite fruits: ")
list_fruit = user_fruits.split(' ')

user_choice = input("please choose a fruit: ")
for i in range(len(list_fruit)):
    if list_fruit[i] == user_choice:
        print("You chose one of your favorite fruits! Enjoy!")
        break
    print("ou chose a new fruit. I hope you enjoy")