import pygame
import torpedo
from settings import *
import sys
import battleship
import random
import math
game_clock = 0
angle = 1.57  # I am in Radians
pygame.init()
clock = pygame.time.Clock()

#FONT CHOICES:
game_font = pygame.font.Font("assets/fonts/Wargate-Normal.ttf", 80)
game_font_big = pygame.font.Font("assets/fonts/Wargate-Normal.ttf", 160)
game_font_small = pygame.font.Font("assets/fonts/Wargate-Normal.ttf", 35)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Torpedo!")
background = pygame.image.load("assets/images/background.png").convert()
title = game_font.render("Torpedo!", True, (0, 0, 0))
background.blit(title, (SCREEN_WIDTH - (title.get_width() + 10), 0))
scoreboard = game_font.render(f"Score:{score}", True, (0, 0, 0))
time = game_font.render(f"Time Left: {game_clock}", True, (0, 0, 0))
background.blit(scoreboard, (SCREEN_WIDTH - (title.get_width() + 10), 60))
background.blit(time, (SCREEN_WIDTH - 700, 125))


for _ in range(NUM_BB):
    HEIGHT_VARY = random.randint(WATER_HEIGHT, LOW_HEIGHT)
    battleship.battleships.add(battleship.Battleship(random.randint(0, SCREEN_WIDTH), HEIGHT_VARY))

def Increase_Angle(angle):
    angle += .1
    return angle

def Decrease_Angle(angle):
    angle -= .1
    return angle


while len(battleship.battleships) > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                torpedo.torpedoes.add(torpedo.Torpedo(angle))
            if event.key == pygame.K_LEFT:
                angle += .1
            if event.key == pygame.K_RIGHT:
                angle -= .1
            if angle >= LAB:
                angle = LAB
            if angle <= RAB:
                angle = RAB
        if angle >= LAB:
            angle = LAB
        if angle <= RAB:
            angle = RAB

        for fired_torpedo in torpedo.torpedoes:
            if fired_torpedo.rect.y <= WATER_HEIGHT:
                torpedo.torpedoes.remove(fired_torpedo)

        for missed_ship in battleship.battleships:
            if missed_ship.rect.x <= 0-220 or missed_ship.rect.x >= SCREEN_WIDTH:
                battleship.battleships.remove(missed_ship)

    sunk_ships = pygame.sprite.groupcollide(torpedo.torpedoes, battleship.battleships, True, True)
    score += len(sunk_ships)
    #if len(chomped_minnows) > 0:
        #print(f"Chomped a minnow, your score is {score}!")

    for sunk_ship in sunk_ships:
        print("I sunk a ship")
        #sounds.explosion.play()

    #pygame.draw.line(screen, (0,0,0), (SCREEN_WIDTH/2, SCREEN_HEIGHT), (SCREEN_WIDTH/2, WATER_HEIGHT), width= 15)



    screen.blit(background, (0, 0))
    torpedo.torpedoes.update()
    battleship.battleships.update()
    torpedo.torpedoes.draw(screen)
    battleship.battleships.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    game_clock += 1/60
print("you are done")