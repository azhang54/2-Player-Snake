'''
Created on Apr 4, 2018

@author: 19ZhangA
'''
import pygame as p
import Variables

class Part(object):
    '''
    A class for each piece of the snake
    '''
    
    def __init__(self, x, y):
       self.x = x
       self.y = y
       
    def draw(self, screen):
        p.draw.rect(screen, p.Color('blue'), p.Rect(self.x*Variables.SQ_SIZE, self.y*Variables.SQ_SIZE, Variables.SQ_SIZE - 2, Variables.SQ_SIZE - 2))