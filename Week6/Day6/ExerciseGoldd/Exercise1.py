# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 12:08:23 2021

@author: lenovo
"""

birthdays = {}
for person in range(5):
    birthdays.update({input("name? "): input("birthday date? ")})

print("You can look up the birthdays of the people in the list!")
user_choice = input("Please enter a name: ")
user_choice.lower()

for x in birthdays.keys():
    if x == user_choice:
        print(f'{user_choice} is born in {birthdays[x]}')

