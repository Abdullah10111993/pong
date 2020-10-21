import pygame
import sys

# initialize pygame
pygame.init()

#screen size
screen_size = (800,600)
screen = pygame.display.set_mode(screen_size)

# window caption
pygame.display.set_caption('Pong')

# loop to continue the game
close_window = False
while not close_window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window = True
    
    #create ball
    ball_color = pygame.Color('white')
    ball_pos = (400,300)
    ball_radius = 20
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    
    #create left pad
    pad_color = pygame.Color('white')
    pad_left = 100
    pad_top = 200
    pad_width = 30
    pad_height = 200 
    pad_params = pygame.Rect(pad_left, pad_top, pad_width, pad_height)
    pygame.draw.rect(screen, pad_color, pad_params)
    

    #create rigth pad
    pad_color = pygame.Color('white')
    pad_left = 700
    pad_top = 200
    pad_width = 30
    pad_height = 200 
    pad_params = pygame.Rect(pad_left, pad_top, pad_width, pad_height)
    pygame.draw.rect(screen, pad_color, pad_params)
        
    #display everything on the screen
    pygame.display.flip()