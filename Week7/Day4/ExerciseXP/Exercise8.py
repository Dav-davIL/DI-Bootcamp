# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 16:23:40 2021

@author: lenovo
"""

def function(number):
    
    formula = 'X+XX+XXX+XXXX'
    formula_list = formula.split("+")
    result_intermediate = [0] * len(formula_list)
    i = len(formula_list) - 1
    result = [0] * len(result_intermediate)
    result_final = ''
    
    while (i >= 0):
        X_number = formula_list[i].count('X')
        result_intermediate[i] = X_number * int(number)
        if result_intermediate[i] >= 10:
            result[i] += result_intermediate[i]%10
            result[i-1] = result_intermediate[i]//10
        else:
            result[i] += result_intermediate[i] 
            if result[i] >= 10:
                result[i-1] =  result[i]//10 
                result[i] = result[i]%10
        i -= 1
    
    
    for k in range(len(result)):
        result_final += str(result[k])
    return result_final
    
            
        
        
        
print(function(3))
