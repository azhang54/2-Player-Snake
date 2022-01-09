'''
Created on Apr 4, 2018

@author: 19ZhangA
'''
import pygame as p
import random as r
import Variables

class Food(object):
    
    def __init__(self):
       self.x = r.randint(0, Variables.NUM_SQ - 1)
       self.y = r.randint(0, Variables.NUM_SQ - 1)
       
    def draw(self, screen):
        p.draw.rect(screen, p.Color('red'), p.Rect(self.x*Variables.SQ_SIZE, self.y*Variables.SQ_SIZE, Variables.SQ_SIZE - 2, Variables.SQ_SIZE - 2))
        