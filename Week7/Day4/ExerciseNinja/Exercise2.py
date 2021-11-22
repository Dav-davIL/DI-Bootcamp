# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 19:40:14 2021

@author: lenovo
"""

class Farm:
    
    def __init__(self,name):
        self.name = name
        self.animals = {}
        
        
    def add_animal(self,type_of_animal,number = 1):
        if type_of_animal in self.animals.keys():
            counter = self.animals[type_of_animal] + number
            self.animals.update({type_of_animal : counter})
        else:
            self.animals.update({type_of_animal : number})
        
   
    def get_info(self):
        print(f'{self.name}\'s farm')
        for key,value in self.animals.items():
            print(key,":", value)
        return '\n\tE-I-E-I-0!'
    
    def get_animal_types(self):
        list_animal = list(self.animals.keys())
        for i in range(len(list_animal)):
            for j in range(i+1, len(list_animal)):
                if list_animal[i] > list_animal[j]:
                    temp = list_animal[i]
                    list_animal[i] = list_animal[j]
                    list_animal[j] = temp
        return list_animal
    
    def get_short_info(self):
        my_list = Farm.get_animal_types(self)
        text = self.name + 's farm has '
        for i in range(len(my_list)):
            if i == len(my_list)-1:
                text += 'and ' + my_list[i]
            else:
                text += my_list[i]+'s' + ' '
        return text

        
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
print(macdonald.get_info())


