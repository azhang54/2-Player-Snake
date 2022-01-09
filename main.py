'''
Created on Apr 4, 2018

@author: 19ZhangA
'''

import pygame as p
import Variables, Part, Food, Scoreboard

def main():
    p.init()
#     screen = p.display.set_mode([Variables.WIDTH, Variables.HEIGHT + ButtonPanel.HEIGHT])
    screen = p.display.set_mode([Variables.WIDTH, Variables.HEIGHT + 100])
    p.display.set_caption('Snake')
    screen.fill((255, 255, 255))
    clock = p.time.Clock()
    
    food = []
    food.append(spawnFood())
    '''
    snake with head at snake[len(snake) - 1]
    '''
    snake1 = [Part.Part(1, 1)]
    snake2 = [Part.Part(Variables.NUM_SQ - 2, Variables.NUM_SQ - 2)]
   
    running = True
    moving = False
    
    while running:
        
        food[0].draw(screen)
        snake1[0].draw(screen)
        snake2[0].draw(screen)
        Scoreboard.draw(screen)
        
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False            
            elif event.type == p.KEYDOWN:
                if event.key == p.K_UP or event.key == p.K_DOWN or event.key == p.K_LEFT or event.key == p.K_RIGHT or event.key == p.K_w or event.key == p.K_a or event.key == p.K_s or event.key == p.K_d:
                    moving = True
                if event.key == p.K_UP and Variables.FACING1 != 'down':
                    Variables.FACING1 = 'up'
                elif event.key == p.K_DOWN and Variables.FACING1 != 'up':
                    Variables.FACING1 = 'down'
                elif event.key == p.K_RIGHT and Variables.FACING1 != 'left':
                    Variables.FACING1 = 'right'
                elif event.key == p.K_LEFT and Variables.FACING1 != 'right':
                    Variables.FACING1 = 'left'
                    
                if event.key == p.K_w and Variables.FACING2 != 'down':
                    Variables.FACING2 = 'up'
                elif event.key == p.K_s and Variables.FACING2 != 'up':
                    Variables.FACING2 = 'down'
                elif event.key == p.K_d and Variables.FACING2 != 'left':
                    Variables.FACING2 = 'right'
                elif event.key == p.K_a and Variables.FACING2 != 'right':
                    Variables.FACING2 = 'left'
            
        if moving:            
            grow(snake1, food)
            grow(snake2, food)
            move(snake1)
            move2(snake2)
            if snake1[len(snake1) - 1].x == snake2[len(snake2) - 1].x and snake1[len(snake1) - 1].y == snake2[len(snake2) - 1].y:
                if len(snake1) > len(snake2):
                    moving = False
                    Variables.P1WINS += 1
                    snake1 = []
                    snake1 = [Part.Part(1, 1)]
                    snake2 = []
                    snake2 = [Part.Part(Variables.NUM_SQ - 2, Variables.NUM_SQ - 2)]
                    food = []
                    food.append(spawnFood())
                    Variables.FACING1 = 'right'
                    Variables.FACING2 = 'left'
                elif len(snake1) < len(snake2):
                    moving = False
                    Variables.P2WINS += 1
                    snake1 = []
                    snake1 = [Part.Part(1, 1)]
                    snake2 = []
                    snake2 = [Part.Part(Variables.NUM_SQ - 2, Variables.NUM_SQ - 2)]
                    food = []
                    food.append(spawnFood())
                    Variables.FACING1 = 'right'
                    Variables.FACING2 = 'left'
                else:
                    moving = False
                    snake1 = []
                    snake1 = [Part.Part(1, 1)]
                    snake2 = []
                    snake2 = [Part.Part(Variables.NUM_SQ - 2, Variables.NUM_SQ - 2)]
                    food = []
                    food.append(spawnFood())
                    Variables.FACING1 = 'right'
                    Variables.FACING2 = 'left'
            elif gameOver(snake1, snake2):
                moving = False
                Variables.P2WINS += 1
                snake1 = []
                snake1 = [Part.Part(1, 1)]
                snake2 = []
                snake2 = [Part.Part(Variables.NUM_SQ - 2, Variables.NUM_SQ - 2)]
                food = []
                food.append(spawnFood())
                Variables.FACING1 = 'right'
                Variables.FACING2 = 'left'
            elif gameOver(snake2, snake1):
                moving = False
                Variables.P1WINS += 1
                snake1 = []
                snake1 = [Part.Part(1, 1)]
                snake2 = []
                snake2 = [Part.Part(Variables.NUM_SQ - 2, Variables.NUM_SQ - 2)]
                food = []
                food.append(spawnFood())
                Variables.FACING1 = 'right'
                Variables.FACING2 = 'left'
            
            p.draw.rect(screen, p.Color('white'), p.Rect(0, 0, Variables.WIDTH, Variables.HEIGHT))
            for f in food:
                f.draw(screen)
            for part in snake1:
                part.draw(screen)
            for part in snake2:
                part.draw(screen)
            Variables.LENGTH1 = len(snake1)
            Variables.LENGTH2 = len(snake2)
            Scoreboard.draw(screen)
            
                
        p.display.flip()
        clock.tick(Variables.MAX_FPS)
        
    p.quit()

def move(snake):
    for i in range(len(snake)):
        if i < len(snake) - 1:
            snake[i].x = snake[i + 1].x
            snake[i].y = snake[i + 1].y
            
        elif i == len(snake) - 1:
            if Variables.FACING1 == 'right':
                snake[i].x += 1
            if Variables.FACING1 == 'left':
                snake[i].x -= 1
            if Variables.FACING1 == 'up':
                snake[i].y -= 1
            if Variables.FACING1 == 'down':
                snake[i].y += 1
                
def move2(snake):
    for i in range(len(snake)):
        if i < len(snake) - 1:
            snake[i].x = snake[i + 1].x
            snake[i].y = snake[i + 1].y
            
        elif i == len(snake) - 1:
            if Variables.FACING2 == 'right':
                snake[i].x += 1
            if Variables.FACING2 == 'left':
                snake[i].x -= 1
            if Variables.FACING2 == 'up':
                snake[i].y -= 1
            if Variables.FACING2 == 'down':
                snake[i].y += 1

def grow(snake, food):
    if snake[len(snake) - 1].x == food[0].x and snake[len(snake) - 1].y == food[0].y:
        food.append(spawnFood())
        food.remove(food[0])
        for i in range(0, 3):
            snake.insert(0, Part.Part(snake[0].x, snake[0].y))

def spawnFood():
    return Food.Food()
        
def gameOver(snake, other):
    #snake head out of bounds
    if snake[len(snake) - 1].x > Variables.NUM_SQ - 1 or snake[len(snake) - 1].x < 0:
        return True
    elif snake[len(snake) - 1].y > Variables.NUM_SQ - 1 or snake[len(snake) - 1].y < 0:
        return True
    #snake overlapping itself or other snake
    else:
        for part in other:
            if snake[len(snake) - 1].x == part.x and snake[len(snake) - 1].y == part.y:
                return True
        if len(snake) > 1:
            for i in range(0, len(snake) - 2):
                if snake[i].x == snake[len(snake) - 1].x and snake[i].y == snake[len(snake) - 1].y:
                    return True
    return False
        
main()