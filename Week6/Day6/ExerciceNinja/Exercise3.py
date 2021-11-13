# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 23:40:58 2021

@author: lenovo
"""

users = {
    "david" : "secret",
    "yael"  : "topsecret",
    "avital": "supersecret"
    }

logged_in  = ''
user_input = input("exit or login? ")
if user_input == "login":
    signup = input("Do you want to sign up? (Y/N) ")
    if signup == 'Y':
        username_input = input("What is your username? ")
        condition = True
        while (condition):
            for y in users.keys():
                if y == username_input:
                    username_input = input("What is your username? ")
            condition = False
        password_input = input("Please enter your password: ")
        users.update({username_input:password_input})
                    
                    
                        
        
    else:
        username = input("username? ")
        password = input("password? ")
        for x in users.keys():
            if username == x:
                print("you are now logged in")
            if password == users.get(username):
                logged_in = username
