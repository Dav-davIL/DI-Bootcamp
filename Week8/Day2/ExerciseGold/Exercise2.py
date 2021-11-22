# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 21:04:22 2021

@author: lenovo
"""

class MyList:
    
    def __init__(self,letters):
        self.letters = letters
        
    def reversedList(self):
        print(self.letters[::-1])
        
    def sortedList(self):
        for i in range(len(self.letters)):
            for j in range(i+1,len(self.letters)):
                if self.letters[i]>self.letters[j]:
                    temp = self.letters[i]
                    self.letters[i] = self.letters[j]
                    self.letters[j] = temp
        print(self.letters)
        
FirstName = MyList(['d','a','v','i','d'])
FirstName.reversedList()
FirstName.sortedList()