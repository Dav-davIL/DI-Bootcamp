# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 15:42:23 2021

@author: illouz
"""
import random

def generateRandomIntegers(number):
    random_number = random.randint(1,100)
    
    if number == random_number:
        print("Great, you success")
    else:
        print(f"You failed! \n {number} != {random_number}")    

generateRandomIntegers(26)