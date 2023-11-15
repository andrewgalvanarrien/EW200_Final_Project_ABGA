import pygame
import destroyer
import torpedo
from settings import *
import sys
import battleship
import sub
import random
game_clock = 0
angle = 1.57 # I am in Radians
pygame.init()
clock = pygame.time.Clock()
# score =

game_font = pygame.font.Font("assets/fonts/Wargate-Normal.ttf", 80)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Torpedo!")
background = pygame.image.load("assets/images/background.png").convert()

title = game_font.render("Torpedo!", True, (0, 0, 0))
background.blit(title, (SCREEN_WIDTH - (title.get_width()+ 10), 0))


my_torpedo = torpedo.Torpedo(angle)
my_battleship = battleship.Battleship(600, hvary)
my_destroyer = destroyer.Destroyer(600, hvary)
my_sub = sub.Sub(600, hvary)
for _ in range(NUM_BB):
    battleship.battleships.add(battleship.Battleship(random.randint(0, SCREEN_WIDTH), hvary))


while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0,0))
    my_torpedo.update()
    my_battleship.update()
    my_destroyer.update()
    my_sub.update()
    battleship.battleships.update()
    my_torpedo.draw(screen)
    my_battleship.draw(screen)
    my_destroyer.draw(screen)
    my_sub.draw(screen)
    battleship.battleships.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    game_clock+= 1/60




# for a ship moving left
# if self.rect.right < 0:
    #append to list of missed_ships