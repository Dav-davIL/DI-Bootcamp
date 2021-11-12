# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 11:11:36 2021

@author: lenovo
"""

users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]

disney_user_A = {}
disney_user_B = {}
disney_user_C = {}
for A in range(len(users)):
    disney_user_A.update({users[A]: A})
    disney_user_B.update({A: users[A]})
print(disney_user_A)
print(disney_user_B)


users.sort()
for C in range(len(users)):
    disney_user_C.update({users[C]: C})
print(disney_user_C)

# The characters, which names contain the letter “i”.
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
disney_user_i = {}
for A in range(len(users)):
    if users[A].find("i") != -1:
        disney_user_i.update({users[A]: A})
print(disney_user_i)

# The characters, which names start with the letter “m” or “p”.
users = [ "Mickey", "Minnie", "Donald","Ariel","Pluto"]
disney_user_mp = {}
for A in range(len(users)):
    user = users[A].lower()
    if user.find("m") != -1 or user.find("p") != -1:
        disney_user_mp.update({users[A]: A})
print(disney_user_mp)