# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 20:10:07 2021

@author: illou
"""

import math

C = 50
H = 30
D_values = input("please input a comma-separated string of numbers: ")
D_list = D_values.split(",")
Q = []

for y in range(len(D_list)):
    D = int(D_list[y])
    Formula = math.floor(math.sqrt((2*C*D)/H))
    Q.append(str(Formula))
    


result = ",".join(Q)
print(result)
