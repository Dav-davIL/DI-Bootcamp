# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 12:40:43 2021

@author: illouz
"""



user = 3;
user_list = []
i = 0
max = -100000000;
while i<user:
    user_number = input("Please enter a number: ");
    if user_number.isdigit():
        user_list.append(int(user_number))
        i += 1

print("Test Data")
for x in range(len(user_list)):
    print("Input number", x, ": ",user_list[x])
    if int(user_list[x])>max:
        max = int(user_list[x])

print(f"The greatest number is: {max} ")
    