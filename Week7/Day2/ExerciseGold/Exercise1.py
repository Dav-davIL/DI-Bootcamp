# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 16:29:23 2021

@author: illouz
"""
import random
def get_random_temp(season):
    if season == 'winter':
        return random.randint(-10, 16)
    elif season == 'spring':
        return random.randint(17, 23)
    elif season == 'summer':
        return random.randint(33, 40)
    elif season == 'spring':
        return random.randint(24,32)

def main():
    season = input("Season ? ")
    temp = get_random_temp(season)
    print(f'The temperature right now is {temp} degrees Celsius.')
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif temp >= 0 and temp < 16:
        print("Quite chilly! Don’t forget your coat")
    elif temp >= 16 and temp < 23:
        print("the temperature is nice")
    elif temp >= 23 and temp < 32:
        print("It's very hot")
    elif temp >= 32 and temp < 40:
        print("it's too hot")

main()
