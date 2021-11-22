# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 19:09:57 2021

@author: lenovo
"""

class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for i in range(len(self.lyrics)):
            print(self.lyrics[i])

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()