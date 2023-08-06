import pygame, sys
from startup import startup
screen = startup()

class Object:
    """
    the base template of all instance
    """
    def __init__(self):
        self.presence = True
        self.pos = (0, 0)
        self.velo = (0, 0)
        self.pace = 10

    def update(self):
        self.pos = (self.pos[0] + self.velo[0],
                    self.pos[1] + self.velo[1])

    def move_up(self):
        self.velo = (self.velo[0], self.pace)

    def move_down(self):
        self.velo = (self.velo[0], -self.pace)

    def move_left(self):
        self.velo = (-self.pace, self.velo[1])

    def move_right(self):
        self.velo = (self.pace, self.velo[1])

    def move_stop(self):
        self.velo = (0, 0)
        
class Player(Object):
    def __init__(self):
        super().__init__()
        self.sprite = screen.blit(pygame.image.load('pika.jpg'), self.pos)
        self.test = 10
        
    