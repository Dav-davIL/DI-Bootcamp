# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def encrypt(text):
    if text != '':
        text = text.upper()
        text_encrypted = ''
        my_list = text.split(" ")
        for word in range(len(my_list)):
            for letter in range(len(my_list[word])):
                text_encrypted += MORSE_CODE_DICT[my_list[word][letter]] + ' '
            text_encrypted += ' / '
        return text_encrypted
    
textEncrypted = encrypt("david illouz")

def decrypt(text_morse):
    if text_morse != '':
        list_morse = text_morse.split(" / ")
        for word in range(len(list_morse)):
            for letter in range(len(list_morse[word])):
                print(list_morse[word][letter])

decrypt('-.. .- ...- .. -..  / .. .-.. .-.. --- ..- --..  /')