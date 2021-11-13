# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 21:13:03 2021

@author: lenovo
"""

items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }

items_list = list(items.keys())
print(f'We have {len(items)} articles: \n {items_list[0]}: {items[items_list[0]]} \n {items_list[1]}: {items[items_list[1]]} \n {items_list[2]}: {items[items_list[2]]} \n {items_list[3]}: {items[items_list[3]]} ')