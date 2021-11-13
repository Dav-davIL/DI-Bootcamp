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
    username = input("username? ")
    password = input("password? ")
    for x in users.keys():
        if username == x:
            print("you are now logged in")
        if password == users.get(username):
            logged_in = username
