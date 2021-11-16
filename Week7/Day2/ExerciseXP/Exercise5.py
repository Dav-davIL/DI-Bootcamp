# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 15:49:01 2021

@author: illouz
"""

def make_shirt(size, message):
    if size == 'L' or size == 'M':
        message = 'I love python'
    print(f'the size of the shirt is {size}. We can see this message: {message}')

make_shirt("L", 'I love python')
make_shirt("M", 'I love python')
make_shirt("S", 'python')
