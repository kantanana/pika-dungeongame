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
        if event.type == QUIT:
            pygame.quit()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                a.move_left()
            if event.key == pygame.K_RIGHT:
                a.move_right()
            if event.key == pygame.K_UP:
                a.move_up()
            if event.key == pygame.K_DOWN:
                a.move_down()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                a.move_stop()
    clock.tick(200)
    pygame.display.update()