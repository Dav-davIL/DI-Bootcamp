# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 19:13:20 2021

@author: lenovo
"""
 
user_input = input("Please enter words separated by comma: ")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
user_list = user_input.split(",")

for i in range(len(user_list)):
    for j in range(i+1, len(user_list)):
        if user_list[i] > user_list[j]:
            temp = user_list[i]
            user_list[i] = user_list[j]
            user_list[j] = temp
            

test = [ user_list[i] 
        for i in range(len(user_list))
            for j in range(i+1, len(user_list))
            if user_list[i] > user_list[j]
        ]