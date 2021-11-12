# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 22:26:30 2021

@author: lenovo
"""

my_text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

text = my_text.split(' ')

for i in range(len(text)):
    print(text[i], text.count(text[i]))