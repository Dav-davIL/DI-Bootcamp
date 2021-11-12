# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 23:26:38 2021

@author: lenovo
"""

basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
basket.pop(0)

# Remove “Blueberries” from the list
basket.pop()

# Add “Kiwi” to the end of the list.
basket.append("Kiwi")

# Add “Apples” to the beginning of the list.
basket.insert(0, "Apples")

# Count how many apples are in the basket
Apples_count = basket.count("Apples")

# Empty the basket
basket = []

print(basket)
