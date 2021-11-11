# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 13:30:24 2021

@author: illouz
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
vowel = 'aeiou'
i= 0
while i < len(alphabet):
    for j in range(len(vowel)):
        if alphabet[i] == vowel[j]:
            print(f"the letter {alphabet[i]} is a vowel")
            i +=1
    print(f"the letter {alphabet[i]} is a consonant")
    i +=1
    

