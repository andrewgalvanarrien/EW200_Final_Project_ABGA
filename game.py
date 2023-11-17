import pygame
import torpedo
from settings import *
import sys
import battleship
import random
game_clock = 0
angle = 1.57     # I am in Radians
pygame.init()
clock = pygame.time.Clock()
score = 0

game_font = pygame.font.Font("assets/fonts/Wargate-Normal.ttf", 80)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Torpedo!")
background = pygame.image.load("assets/images/background.png").convert()

title = game_font.render("Torpedo!", True, (0, 0, 0))
background.blit(title, (SCREEN_WIDTH - (title.get_width() + 10), 0))

my_torpedo = torpedo.Torpedo(angle)

for _ in range(NUM_BB):
    hvary = random.randint(WATER_HEIGHT, LOW_HEIGHT)
    battleship.battleships.add(battleship.Battleship(random.randint(0, SCREEN_WIDTH), hvary))



while True:
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

        for fired_torpedo in torpedo.torpedoes:
            if torpedo.rect.y <= WATER_HEIGHT:
                torpedo.torpedoes.remove(fired_torpedo)

    sunk_ships = pygame.sprite.spritecollide(my_torpedo, battleship.battleships, True)
    score += len(sunk_ships)
    #if len(chomped_minnows) > 0:
        #print(f"Chomped a minnow, your score is {score}!")

    for sunk_ship in sunk_ships:
        print("I sunk a ship")
        #sounds.explosion.play()

    scoreboard = game_font.render(f"Score:{score}", True, (0, 0, 0))
    background.blit(scoreboard, (SCREEN_WIDTH - (title.get_width() + 10), 60))

    screen.blit(background, (0, 0))
    my_torpedo.update()
    torpedo.torpedoes.update()
    battleship.battleships.update()
    torpedo.torpedoes.draw(screen)
    my_torpedo.draw(screen)
    battleship.battleships.draw(screen)
    pygame.display.flip()
    clock.tick(60)
    game_clock += 1/60
