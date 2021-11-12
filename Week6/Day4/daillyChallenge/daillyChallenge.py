# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 06:46:48 2021

@author: lenovo
"""

import datetime
birth_date = input('Give us your birthdate in the following format DD/MM/YYYY: ')
birthdate = datetime.datetime.strptime(birth_date, '%d/%m/%Y')
day, month, year = birth_date.split('/')
current_date = {
     'day': 11,
     'month': 11,
     'year': 2021
}

day, month, year = int(day), int(month), int(year)

age = current_date['year'] - year
if month > current_date['month']:
     age -= 1
elif month == current_date['month'] and day > current_date['day']:
     age -= 1
    
print(f'i am {age} years old')
candles = int(str(age)[-1]) * 'i'
# while len(candles) < 11:
#     candles += '_'
#     print(candles)
candle_string = f"{(11-len(candles))//2 * '_'}{candles}{(11-len(candles))//2 * '_'}"
if len(candle_string) % 2 == 0:
    candle_string += '_'
# candle string should be 11 max
cake = f'''
       {candle_string}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
'''
print(cake)