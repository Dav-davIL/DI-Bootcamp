# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 19:10:33 2021

@author: lenovo
"""

def get_full_name(first_name,last_name, *middle_name):
    total = first_name 
    for arg in middle_name:
        total += ' ' + arg 
    total += ' ' + last_name
    return total
 

print(get_full_name("david","illouz"))
