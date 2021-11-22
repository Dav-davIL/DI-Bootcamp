# -*- coding: utf-8 -*-
"""
Created on Sun Nov 21 19:37:46 2021

@author: lenovo
"""

class Farm:
    
    def __init__(self, farm_name):
        self.farm_name = farm_name
        self.animals = {}
    
    def add_animal(self, animal_type, mount=1):
        if animal_type in self.animals:
            self.animals[animal_type] = self.animals[animal_type] + mount
        else:
            self.animals[animal_type] = mount
    
    def get_info(self):
        print(f"{self.farm_name}'s farm\n")
        
        for animal_type, animal_mount in self.animals.items():
            print(f'{animal_type}: {animal_mount}')

        return '\n\tE-I-E-I-0!'
    
    def get_animal_types(self):
        myList = list(self.animals.keys())
        
        for i in range(len(myList)):
            for j in range(i+1,len(myList)):
                if myList[i] > myList[j]:
                    temp = myList[i]
                    myList[i] = myList[j]
                    myList[j] = temp
        return myList
    
    def get_short_info(self):
        list_animals = Farm.get_animal_types(self)
        text = self.farm_name + '\'s farm has '
        for i in range(len(list_animals)):
            if i == len(list_animals)-1:
                text += 'and '+list_animals[i]
            else:
                text += list_animals[i] + ' '
        print(text)
            
macdonald = Farm("McDonald")
macdonald.add_animal('cow',5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
macdonald.get_short_info()