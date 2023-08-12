import pygame, sys
from pygame.locals import QUIT
from startup import startup
try:
    from objects import Player, screen
except:
    AssertionError()

clock = pygame.time.Clock()
running = True
pygame.display.set_caption('Pika game')
a = Player()

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
    clock.tick(200)
    pygame.display.update()