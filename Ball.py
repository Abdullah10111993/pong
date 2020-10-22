import pygame


class Ball:
    def __init__(self, ball_pos, ball_color, ball_velocity, ball_radius, screen):
        self.pos = ball_pos
        self.color = pygame.Color(ball_color)
        self.velocity = ball_velocity
        self.radius = ball_radius
        self.screen = screen
        self.shape = None
        
    def move(self):
        screen_size = self.screen.get_size()
        
        for index in range(len(self.pos)):
            self.pos[index] += self.velocity[index]
            
        # bounce ball
        if self.pos[0] < 0 or self.pos[0] > screen_size[0]:
            self.velocity[0] = -self.velocity[0]
        if self.pos[1] < 0 or self.pos[1] > screen_size[1]:
            self.velocity[1] = -self.velocity[1]         

    def move_after_colision(self):
        self.velocity[0] = -self.velocity[0]
        
    def draw(self):
        self.shape = pygame.draw.circle(self.screen, self.color, self.pos, self.radius)        