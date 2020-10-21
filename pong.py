import pygame
import sys
from Ball import Ball 
from Pad import Pad

# initialize pygame
pygame.init()

#screen size
screen_size = (800,600)
screen = pygame.display.set_mode(screen_size)

# window caption
pygame.display.set_caption('Pong')

bg_color = pygame.Color('black')
fps = 120
game_clock = pygame.time.Clock()

# ball initial pos
ball_pos = [400,300]
ball_color = 'white'
ball_velocity = [1,1]
ball_radius = 20   
ball = Ball(ball_pos, ball_color, ball_velocity, ball_radius, screen)

pad_color = pygame.Color('white')

#create rigth pad
right_pad_left = 700
right_pad_top = 200
right_pad_width = 30
right_pad_height = 200 
right_pad = Pad(right_pad_left, right_pad_top, right_pad_width, right_pad_height, pad_color, screen)

#create left pad
left_pad_left = 100
left_pad_top = 200
left_pad_width = 30
left_pad_height = 200 
left_pad = Pad(left_pad_left, left_pad_top, left_pad_width, left_pad_height, pad_color, screen)

# loop to continue the game
close_window = False
while not close_window:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            close_window = True
    
        if event.type == pygame.KEYDOWN and event.__dict__['key'] == 119:
            print(event.__dict__['key'])
            right_pad.move_up()
    
        if event.type == pygame.KEYDOWN and event.__dict__['key'] == 115:
            print(event.__dict__['key'])
            right_pad.move_down()   
    
        if event.type == pygame.KEYDOWN and event.__dict__['key'] == 273:
            print(event.__dict__['key'])
            left_pad.move_up()
    
        if event.type == pygame.KEYDOWN and event.__dict__['key'] == 274:
            print(event.__dict__['key'])
            left_pad.move_down()         
            
    #create ball
    screen.fill(bg_color)
    
    ball.draw()
    ball.move()       

    #create right pad
    right_pad.draw()
    #create left pad
    left_pad.draw()
    
    #render score
    score = 0
    score_text = 'score:'+str(score)
    text_color = pygame.Color('white')
    text_font = pygame.font.SysFont('Times New Roman',30)
    score_image = text_font.render(score_text, True, text_color)
    score_pos = (0,0)
    screen.blit(score_image, score_pos)
    
    #display everything on the screen
    pygame.display.flip()
    game_clock.tick(fps)