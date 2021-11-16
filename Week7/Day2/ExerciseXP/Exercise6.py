# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 16:01:56 2021

@author: illouz
"""

magicians_list = ['clown', 'abracadabra', 'noidea']

def show_magicians(magicians_list):
    for i in range(len(magicians_list)):
        print(make_great(magicians_list[i]))

def make_great(text):
    return "the Great " + text

show_magicians(magicians_list)
    