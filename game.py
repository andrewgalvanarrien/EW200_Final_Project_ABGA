import pygame
import random
import destroyer
from settings import *
import sys
import battleship
import cruiser

pygame.init()
clock = pygame.time.Clock()
# score =
hvary= random.randint(WATER_HEIGHT, LOW_HEIGHT)
game_font = pygame.font.Font("assets/fonts/Wargate-Normal.ttf", 80)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Torpedo!")
background = pygame.image.load("assets/images/background.png").convert()

title = game_font.render("Torpedo!", True, (0, 0, 0))
background.blit(title, (SCREEN_WIDTH - (title.get_width()+ 10), 0))

my_battleship = battleship.Battleship(200, WATER_HEIGHT)
my_destroyer = destroyer.Destroyer(400, WATER_HEIGHT)
my_cruiser = cruiser.Cruiser(300, hvary)

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0,0))
    my_battleship.draw(screen)
    my_destroyer.draw(screen)
    my_cruiser.draw(screen)
    my_battleship.update()
    my_destroyer.update()
    my_cruiser.update()
    pygame.display.flip()
    clock.tick(60)




# for a ship moving left
# if self.rect.right < 0:
    #append to list of missed_ships