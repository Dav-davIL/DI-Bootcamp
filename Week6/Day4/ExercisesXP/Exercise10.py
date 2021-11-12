# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 06:45:23 2021

@author: lenovo
"""
list_toppings = []
price_toppings = 0
price_pizza = 0
user_toppings = input("Please enter your toppings ('quit' to stop): ")
list_toppings.append(user_toppings)
while (user_toppings != 'quit'):
    user_toppings = input("you’ll add that topping to their pizza: ")
    list_toppings.append(user_toppings)
    
for i in range(len(list_toppings)):
    print(list_toppings[i])
    price_toppings += 2.5
price_pizza = 10 + price_toppings

print(price_pizza)