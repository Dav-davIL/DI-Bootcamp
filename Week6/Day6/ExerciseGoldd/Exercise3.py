# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 21:08:34 2021

@author: lenovo
"""

birthdays = {}
for person in range(1):
    birthdays.update({input("name? "): input("birthday date? ")})

print("Please add your birthday date!")
key = input("Please enter your name: ")
value = input("please enter your birthday date  (in the format “YYYY/MM/DD”): ")

birthdays.update({key:value})

print("You can look up the birthdays of the people in the list!")
print(birthdays.keys())
user_choice = input("Please enter a name: ")
user_choice.lower()

birthday_list = list(birthdays.keys())
#for x in range(len(birthday_list)):
x = 0
while (x < len(birthdays)):
    if birthday_list[x] == user_choice:
        print(f'{user_choice} is born in {birthdays[birthday_list[x]]}')
        break
    elif x == len(birthdays)-1:
        print("Sorry, we don’t have the birthday information for ", user_choice)
    x += 1