# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 21:33:02 2021

@author: lenovo
"""

my_string = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet"
my_list = my_string.split(",")

print(f'In the list, we have {len(my_list)} companies')

my_list.sort(reverse=True)
print(my_list)

count_o = 0
count_i = 0
for i in range(len(my_list)):
    if (my_list[i].find("o") != -1):
        count_o +=1
    elif (my_list[i].find("i") == -1):
        count_i +=1

print("manufacturers’ names have the letter ‘o’ in them: ", count_o)
print("manufacturers’ names do not have the letter ‘i’ in them: ", (len(my_list) - count_i))