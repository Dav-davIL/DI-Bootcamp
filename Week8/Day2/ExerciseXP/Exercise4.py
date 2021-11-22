# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 20:11:10 2021

@author: lenovo
"""

class Zoo:
    
    def __init__(self,zoo_name):
        self.animals = []
        self.name = zoo_name
    
    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)
    
    def get_animals(self):
        print(self.animals)
    
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
    
    def sort_animals(self):
        for i in range(len(self.animals)):
            for j in range(i+1,len(self.animals)):
                if self.animals[i]>self.animals[j]:
                    temp = self.animals[i]
                    self.animals[i] = self.animals[j]
                    self.animals[j] = temp
        
        k = 1
        groups = {}
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        while(True):
            for animal in range(len(self.animals)):
                group_of_animals = []
                for letter in range(len(alphabet)):
                    if self.animals[animal][0].lower() == alphabet[letter]:
                        group_of_animals.append(self.animals[animal])
                groups.update({k:group_of_animals})
                k += 1
            break
        return groups
        
    def get_groups(self):
        group = Zoo.sort_animals(self)
        for key, value in group.items():
            print(key, ": ", value)
        

ramat_gan_safari  = Zoo("Ape")
ramat_gan_safari.add_animal("Baboon")
ramat_gan_safari.add_animal('Cat')
ramat_gan_safari.add_animal('Eel')
ramat_gan_safari.add_animal('Bear')
ramat_gan_safari.get_animals()
ramat_gan_safari.sell_animal('Baboon')
ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()
        
                    