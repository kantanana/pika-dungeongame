import pygame, sys
from pygame.locals import QUIT
from startup import startup
from objects import Player, Enemy, screen
from collision import collide

clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Pika game')
a = Player()
b = Enemy()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        a.move_left()
    else:
        a.move_stop()
    if keys[pygame.K_RIGHT]:
        a.move_right()
    else:
        a.move_stop()
    if keys[pygame.K_UP]:
        a.move_up()
    else:
        a.move_stop()
    if keys[pygame.K_DOWN]:
        a.move_down()
    else:
        a.move_stop()
    if keys[pygame.MOUSEBUTTONDOWN]:
        if collide(a.pos, b.pos):
            a.attack()
    b.chase(a)
    clock.tick(200)
    pygame.display.update()