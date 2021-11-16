# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 20:10:44 2021

@author: illouz
"""

user_string = input('Please enter words (separate by coma): ')

def box_printer(amount_string):
    list_string = amount_string.split(", ")
    maximum = -100000000
    text = ''
    for i in range(len(list_string)):
        if len(list_string[i]) > maximum:
            maximum = len(list_string[i])
    
    print('*'*(maximum+4))
    for j in range(len(list_string)):
        if len(list_string[j]) < maximum:
            text = '* ' + list_string[j] + ' ' * (maximum - len(list_string[j])) + ' *'
        elif len(list_string[j]) == maximum:
            text = '* ' + list_string[j]  + ' *'
        print(text)
    print('*'*(maximum+4))

box_printer(user_string)