import pygame
import sys

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
ball_color = pygame.Color('white')
ball_velocity = [1,1]
ball_radius = 20

pad_color = pygame.Color('white')

#create rigth pad
right_pad_left = 700
right_pad_top = 200
right_pad_width = 30
right_pad_height = 200 

#create left pad
left_pad_left = 100
left_pad_top = 200
left_pad_width = 30
left_pad_height = 200 

# loop to continue the game
close_window = False
while not close_window:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_window = True
    
    #create ball
    screen.fill(bg_color)
    pygame.draw.circle(screen, ball_color, ball_pos, ball_radius)
    for index in range(len(ball_pos)):
        ball_pos[index] += ball_velocity[index]
        
    # bounce ball
    if ball_pos[0] < 0 or ball_pos[0] > screen_size[0]:
        ball_velocity[0] = -ball_velocity[0]
    if ball_pos[1] < 0 or ball_pos[1] > screen_size[1]:
        ball_velocity[1] = -ball_velocity[1]    

    #create right pad
    right_pad_params = pygame.Rect(right_pad_left, right_pad_top, right_pad_width, right_pad_height)
    pygame.draw.rect(screen, pad_color, right_pad_params)
    
    #create left pad
    left_pad_params = pygame.Rect(left_pad_left, left_pad_top, left_pad_width, left_pad_height)
    pygame.draw.rect(screen, pad_color, left_pad_params)
    
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