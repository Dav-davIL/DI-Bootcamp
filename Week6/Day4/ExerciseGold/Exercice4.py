# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 15:41:48 2021

@author: illouz
"""

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
for y in range(len(names)):
    names[y] = names[y].lower()
    
#Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
user_name = input("Please what's your name?")
if not(isinstance(user_name,str)):
    print("it's not a string")
else:
    for x in range(len(names)):
        if user_name == names[x]:
            user_name_index = names.index(user_name)
            print(f"if input is '{user_name}' we should be printing the index {user_name_index}")
            break
