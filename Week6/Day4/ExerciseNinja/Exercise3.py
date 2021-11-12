# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 16:34:12 2021

@author: illouz
"""

paragraph = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

charactersLength = len(paragraph)

start = 0
Sentence = 0
point = 0
while (point <= charactersLength):
    if paragraph.find(".", start) != -1:
        point = paragraph.index(".", start)
        start = point + 1
        Sentence += 1
    else:
        point = 10**6
    
wordsLength = len(paragraph.split(" "))

text = paragraph.split(' ')
uniqueWord = 0
for i in range(len(text)):
    if paragraph.count(text[i]) == 1:
        uniqueWord += 1

print("characters: ", charactersLength)
print("Sentences: ", Sentence)
print("words: ",wordsLength)
print("unique words: ",uniqueWord)