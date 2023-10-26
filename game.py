import pygame
from settings import *
import sys
pygame.init()
clock = pygame.time.Clock()
# score =
# game_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", 128)


screen = pygame.display.set_mode((SCREEN_WIDTH2, SCREEN_HEIGHT2))
pygame.display.set_caption("Battle of Surigao Strait")
background = pygame.image.load("assets/images/background.png").convert()

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background, (0,0))
    pygame.display.flip()
    clock.tick(60)
