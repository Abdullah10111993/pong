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
text_font = pygame.font.SysFont('Times New Roman',30)
text_color = pygame.Color('white')
fps = 120
game_clock = pygame.time.Clock()

# ball initial pos
ball_pos = [int(screen_size[0]/2), int(screen_size[1]/2)]
ball_color = 'white'
ball_velocity = [2,2]
ball_radius = 10   
ball = Ball(ball_pos, ball_color, ball_velocity, ball_radius, screen)

pad_color = pygame.Color('white')

#create rigth pad
right_score = 0
right_pad_height = 200
right_pad_left = 670
right_pad_top = 200
right_pad_width = 30 
right_pad = Pad(right_pad_left, right_pad_top, right_pad_width, right_pad_height, pad_color, screen)
right_pad_up = False
right_pad_down = False

#create left pad
left_score = 0
left_pad_height = 200 
left_pad_left = 100
left_pad_top = 200
left_pad_width = 30
left_pad = Pad(left_pad_left, left_pad_top, left_pad_width, left_pad_height, pad_color, screen)
left_pad_up = False
left_pad_down = False

# loop to continue the game
close_window = False
while not close_window:

    screen.fill(bg_color)
    #render score
    left_score_text = 'score:'+str(left_score)
    left_score_image = text_font.render(left_score_text, True, text_color)
    left_score_pos = (0,0)
    screen.blit(left_score_image, left_score_pos)
    
    right_score_text = 'score:'+str(right_score)
    right_score_image = text_font.render(right_score_text, True, text_color)
    right_score_pos = (screen_size[0]-len(right_score_text)*13,0)
    screen.blit(right_score_image, right_score_pos)   
    
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            close_window = True
    
        if event.type == pygame.KEYDOWN and event.__dict__['key'] == 273:
            #print(event.__dict__['key'])
            right_pad_up = True
    
        if event.type == pygame.KEYUP and event.__dict__['key'] == 273:
            #print(event.__dict__['key'])
            right_pad_up = False    

        if event.type == pygame.KEYDOWN and event.__dict__['key'] == 274:
            #print(event.__dict__['key'])
            right_pad_down = True   
            
        if event.type == pygame.KEYUP and event.__dict__['key'] == 274:
            #print(event.__dict__['key'])
            right_pad_down = False             
    
        if event.type == pygame.KEYDOWN and event.__dict__['key'] == 119:
            #print(event.__dict__['key'])
            left_pad_up = True

        if event.type == pygame.KEYUP and event.__dict__['key'] == 119:
            #print(event.__dict__['key'])
            left_pad_up = False     
    
        if event.type == pygame.KEYDOWN and event.__dict__['key'] == 115:
            #print(event.__dict__['key'])
            left_pad_down = True   
        
        if event.type == pygame.KEYUP and event.__dict__['key'] == 115:
            #print(event.__dict__['key'])
            left_pad_down = False     
            
    #create ball
    
    ball.draw()
    ball.move()       
    
    if right_pad_up:
        right_pad.move_up()
        
    if right_pad_down:
        right_pad.move_down()
            
    if left_pad_up:
        left_pad.move_up()        
    
    if left_pad_down:
        left_pad.move_down()
        
    #create right pad
    right_pad.draw()
    #create left pad
    left_pad.draw()
    
    #if right_pad.collision([right_pad.left_pos, right_pad.top_pos], ball.pos, ball.velocity[0]):
        #ball.move_after_colision()

    #if left_pad.collision([left_pad.left_pos+left_pad.width, left_pad.top_pos], ball.pos, ball.velocity[0]*-1):
        #ball.move_after_colision()        
        
    if right_pad.shape.collidepoint(ball.pos[0]+ball.radius, ball.pos[1]) and ball.velocity[0] > 0:
        ball.move_after_colision()
        
    if left_pad.shape.collidepoint(ball.pos[0]-ball.radius, ball.pos[1]) and ball.velocity[0] < 0:
        ball.move_after_colision()        
        
    #if ball.pos[0] - ball.radius == 0:
        #right_score += 1
    #if ball.pos[0] + ball.radius == screen_size[0]:
        #left_score += 1
    if ball.shape.collidepoint(0, ball.pos[1]):
        right_score += 1
    if ball.shape.collidepoint(screen_size[0]-1, ball.pos[1]):
        left_score += 1
    #display everything on the screen
    pygame.display.flip()
    game_clock.tick(fps)