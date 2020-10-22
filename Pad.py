import pygame


class Pad:
    def __init__(self, left_pos, top_pos, width, height, color, screen):
        self.left_pos = left_pos
        self.top_pos = top_pos
        self.width = width
        self.height = height
        self.velocity = 5
        self.screen = screen
        self.pad_color = color
        self.shape = None
        
    def move_up(self):
        if self.top_pos > 0:# and (self.top_pos + self.height) < screen_height:
            self.top_pos -= self.velocity

    def move_down(self):
        screen_height = self.screen.get_height()
        #print(self.top_pos, screen_height)
        if (self.top_pos + self.height) < screen_height:
            self.top_pos += self.velocity
            
    def draw(self):
        pad_params = pygame.Rect(self.left_pos, self.top_pos, self.width, self.height)
        self.shape = pygame.draw.rect(self.screen, self.pad_color, pad_params)     
        
    def collision(self, pointA, pointB, direction):
        if pointB[0] == pointA[0] and pointB[1] >= pointA[1] and pointB[1] >= pointA[1]+self.height and direction > 0:
            return True
        return False