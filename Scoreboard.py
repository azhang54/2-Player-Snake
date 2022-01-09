'''
Created on Apr 6, 2018

@author: 19ZhangA
'''
import pygame as p
import Variables

def draw(screen):
    
    panel = p.Rect(0, Variables.HEIGHT, Variables.WIDTH, 100)
    p.draw.rect(screen, p.Color(0, 0, 0), panel)
    
    font = p.font.SysFont('Comic Sans', 30)
    
    texts = ['Player 1 Wins: ' + str(Variables.P1WINS) + '     ' + 'Player 1 Length: ' + str(Variables.LENGTH1),
             'Player 2 Wins: ' + str(Variables.P2WINS) + '     ' + 'Player 2 Length: ' + str(Variables.LENGTH2)]
    textObjects = []
    textLocations = []
    
    for text in texts:
        textObjects.append(font.render(text, 0, p.Color('white')))
    
    for i in range(len(textObjects)):
        textLocations.append(panel.move(5, 20*i))
        screen.blit(textObjects[i], textLocations[i])
        
        