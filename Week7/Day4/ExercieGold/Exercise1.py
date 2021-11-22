# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 18:25:36 2021

@author: lenovo
"""
import random

def throw_dice():
    return random.randint(1,6)

def throw_until_doubles():
    dice1 = 0
    dice2 = 1
    throw = 0
    while (dice1 != dice2):
        dice1 = throw_dice()
        dice2 = throw_dice()
        throw += 1
    return throw

def main():
    throw_list = []
    addition = 0
    for i in range(100):
        throw_result = throw_until_doubles()
        throw_list.append(throw_result)
        addition += throw_list[i]
    average = addition/100
    average = "{:.2f}".format(average)
    print("throw in total: ", addition)
    print("average ", average)
    
main()