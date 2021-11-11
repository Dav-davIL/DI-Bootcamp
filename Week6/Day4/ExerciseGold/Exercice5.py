# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 16:11:50 2021

@author: illouz
"""
words = []
words_number = 7
i = 0
x = 0

while i < words_number:
    user_word = input("Please enter a word: ")
    user_word = user_word.lower()
    if user_word.isdigit():
        user_word = input("Please enter a word: ")
    else:
        words.append(user_word)
        i += 1

letter = input("Please enter a letter: ")
letter = letter.lower()

while x < len(words):
    for y in range(len(words[x])):
        if letter == words[x][y]:
            position = words[x].index(letter)
            print(letter," is in '",words[x],"' at the position", str(position))
    x += 1
print("We didn't find this letter")    

    
            