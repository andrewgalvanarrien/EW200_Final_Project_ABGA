import pygame
import torpedo
from settings import *
import sys
import battleship
import random
import math
game_clock = 100
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
data_background = pygame.image.load("assets/images/data_background.png").convert()
title = game_font.render("Torpedo!", True, (0, 0, 0))
background.blit(title, (SCREEN_WIDTH - (title.get_width() + 10), 0))
#scoreboard = game_font.render(f"Score: {score}", True, (0, 0, 0))
#time = game_font.render(f"Time Left: {game_clock}", True, (0, 0, 0))
#background.blit(scoreboard, (SCREEN_WIDTH - (title.get_width() + 10), 60))
#sbackground.blit(time, (SCREEN_WIDTH - 500, 125))
#score_msg = game_font.render(f"{score}",True, (0,0,0))

def draw_score():
    background.blit(data_background, (SCREEN_WIDTH-636, 0))
    #background.blit(score_msg, (SCREEN_WIDTH-50, 100))

for _ in range(NUM_BB):
    HEIGHT_VARY = random.randint(WATER_HEIGHT, LOW_HEIGHT)
    battleship.battleships.add(battleship.Battleship(random.randint(0, SCREEN_WIDTH), HEIGHT_VARY))

def Increase_Angle(angle):
    angle += .1
    return angle

def Decrease_Angle(angle):
    angle -= .1
    return angle


while True:
    rotating_left = False
    rotating_right = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                torpedo.torpedoes.add(torpedo.Torpedo(angle))
            if event.key == pygame.K_LEFT:
                rotating_left = True
            if event.key == pygame.K_RIGHT:
                rotating_right = True
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
    screen.blit(background, (0, 0))
    scoreboard = game_font.render(f"Score: {score}", True, (0, 0, 0))
    time = game_font.render(f"Time Left: {game_clock}", True, (0, 0, 0))
    screen.blit(scoreboard, (SCREEN_WIDTH - (title.get_width() + 10), 60))
    screen.blit(time, (SCREEN_WIDTH - 600, 125))

    for sunk_ship in sunk_ships:
        print("I sunk a ship")
        #sounds.explosion.play()

    #draw_score()

    if rotating_left:
        angle += 0.1
    elif rotating_right:
        angle -= 0.1
    torpedo.torpedoes.update()
    battleship.battleships.update()
    torpedo.torpedoes.draw(screen)
    battleship.battleships.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    game_clock -= 1/60
print("you are done")