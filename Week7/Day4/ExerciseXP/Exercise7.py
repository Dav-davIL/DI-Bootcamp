# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 15:05:58 2021

@author: lenovo
"""
import datetime
gender = input("What is your gender? ")
date_of_birth = input("When is your birthday? ")

def get_age(year, month, day):
    now = datetime.datetime.now()
    current_year  = int(now.strftime("%Y"))
    current_month = int(now.strftime("%m"))
    current_day = int(now.strftime("%d"))
    
    age  = current_year - int(year)
    if int(month) > current_month:
        age -= 1
    elif int(month) == current_month and int(day) > current_day:
        age -= 1
     
    return age

def can_retire(gender, date_of_birth):
    year, month, day = date_of_birth.split('/')
    if gender == 'm':
        if get_age(year, month, day) >= 67:
            return True
        else:
            return False
    elif gender == 'f':
        if get_age(year, month, day) >= 62:
            return True
        else:
            return False
    else:
        print("your are not a man or a woman")
    
retire = can_retire(gender, date_of_birth)
if retire == True:
    print("You can retire")
else:
    print("You can't retire")
        
    