# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 19:59:43 2021

@author: lenovo
"""

user_input = input(" Please enter your message: ")
cypher_text = ''

for i in range(len(user_input)):
    if ord(user_input[i])>=97 and  ord(user_input[i])<=122:
        if ord(user_input[i])<=122 and ord(user_input[i])>=120:
            step = 2 - (122 - ord(user_input[i]))
            cypher_text += chr(ord('a') + step)
        else:
            cypher_text += chr(ord(user_input[i]) + 3)
    elif ord(user_input[i])>=65 and  ord(user_input[i])<=90:
        if ord(user_input[i])<=88 and ord(user_input[i])>=90:
            step = 2 - (90 - ord(user_input[i]))
            cypher_text += chr(ord('A') + step)
        else:
            cypher_text += chr(ord(user_input[i]) + 3)
    elif ord(user_input[i]) == 32:
        cypher_text += chr(ord(user_input[i]))

print("Encryption")
print(cypher_text)

print('Decryption')
user_input = cypher_text
text = ''
for i in range(len(user_input)):
    if ord(user_input[i])>=97 and  ord(user_input[i])<=122:
        if ord(user_input[i])<=99 and ord(user_input[i])>=97:
            step = 2 - (ord(user_input[i])-97)
            text += chr(ord('z') - step)
        else:
            text += chr(ord(user_input[i]) - 3)
    elif ord(user_input[i])>=65 and  ord(user_input[i])<=90:
        if ord(user_input[i])<=63 and ord(user_input[i])>=65:
            step = 2 - (ord(user_input[i])- 65)
            text += chr(ord('Z') - step)
        else:
            text += chr(ord(user_input[i]) - 3)
    elif ord(user_input[i]) == 32:
        text += chr(ord(user_input[i]))
print(text) 
           
    