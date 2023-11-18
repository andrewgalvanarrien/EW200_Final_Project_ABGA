import pygame
from settings import *
import sys
pygame.init()

game_font_big = pygame.font.Font("assets/fonts/Wargate-Normal.ttf", 160)
game_font_small = pygame.font.Font("assets/fonts/Wargate-Normal.ttf", 35)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Torpedo!")
background = pygame.image.load("assets/images/background.png").convert()
title = game_font_big.render("Torpedo!", True, (0, 0, 0))
begin = game_font_small.render("Press 'ENTER' to Start", True, (0, 0, 0))
background.blit(title, (SCREEN_WIDTH/2 - (title.get_width()/2), SCREEN_HEIGHT/2 - 45))
background.blit(begin, (SCREEN_WIDTH/2 - (begin.get_width()/2), SCREEN_HEIGHT/2 + 100))

while True:
    screen.blit(background, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
