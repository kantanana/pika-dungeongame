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
        self.pace = 1
        self.sprite = None
        self.black = None

    def update(self):
        screen.blit(self.black, self.pos)
        self.pos = (self.pos[0] + self.velo[0],
                    self.pos[1] + self.velo[1])
        screen.blit(self.sprite, self.pos)

    def move_down(self):
        self.velo = (self.velo[0], self.pace)
        self.update()

    def move_up(self):
        self.velo = (self.velo[0], -self.pace)
        self.update()

    def move_left(self):
        self.velo = (-self.pace, self.velo[1])
        self.update()

    def move_right(self):
        self.velo = (self.pace, self.velo[1])
        self.update()

    def move_stop(self):
        self.velo = (0, 0)
        self.update()
        
class Player(Object):
    def __init__(self):
        super().__init__()
        self.sprite = pygame.image.load('pika.jpg')
        self.black = pygame.image.load('black_50by50.jpg')
        self.test = 10
        self.hp = 100
        self.attack = 5

    def attack(self, target):
        target.hp -= self.attack

class Enemy(Object):
    def __init__(self):
        super().__init__()
        self.sprite = pygame.image.load('pika.jpg')
        self.black = pygame.image.load('black_50by50.jpg')
        self.test = 10
        self.hp = 100
        self.attack = 5

    def chase(self, player):
        if self.pos[0] > player.pos[0]:
            self.move_left()
        elif self.pos[0] < player.pos[0]:
            self.move_right()
        elif self.pos[1] > player.pos[1]:
            self.move_up()
        elif self.pos[1] < player.pos[1]:
            self.move_down()
    
        
    