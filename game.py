import pygame
from settings import *
import sys
import battleship

pygame.init()
clock = pygame.time.Clock()
# score =
game_font = pygame.font.Font("assets/fonts/Wargate-Normal.ttf", 80)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Torpedo!")
background = pygame.image.load("assets/images/background.png").convert()

title = game_font.render("Torpedo!", True, (0, 0, 0))
background.blit(title, (SCREEN_WIDTH - (title.get_width()+ 10), 0))

my_battleship = battleship.Battleship(200,200)


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0,0))
    my_battleship.draw(screen)
    pygame.display.flip()
    clock.tick(60)
