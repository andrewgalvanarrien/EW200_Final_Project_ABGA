import pygame
import torpedo
from settings import *
import sys
import battleship
import random
pygame.init()

# INITIAL VARIABLES
angle = 1.57  # in Radians
high_score = 0
clock = pygame.time.Clock()

# FONT CHOICES:
game_font = pygame.font.Font("assets/fonts/Wargate-Normal.ttf", 80)
game_font_big = pygame.font.Font("assets/fonts/Wargate-Normal.ttf", 160)
game_font_small = pygame.font.Font("assets/fonts/Wargate-Normal.ttf", 35)
game_font_medbig = pygame.font.Font("assets/fonts/Wargate-Normal.ttf", 130)
game_font_med = pygame.font.Font("assets/fonts/Wargate-Normal.ttf", 55)

# SCREEN BTS
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Torpedo!")
background = pygame.image.load("assets/images/background.png").convert()
data_background = pygame.image.load("assets/images/data_background.png").convert()

# RENDERS
title = game_font.render("Torpedo!", True, (0, 0, 0))
begin = game_font_small.render("Press 'ENTER' to Start", True, (0, 0, 0))
big_title = game_font_big.render("Torpedo!", True, (0, 0, 0))
GO = game_font_medbig.render("GAME OVER!", True, (0, 0, 0))
HIGH_SCORE = game_font_med.render(f"HIGH SCORE: {high_score}", True, (0, 0, 0))
GO_BACK = game_font_med.render("Press 'ENTER' to Return to Start", True, (0, 0, 0))


def increase_angle(angle):
    angle += .1
    return angle


def decrease_angle(angle):
    angle -= .1
    return angle


# The Game
while True:
    screen.blit(background, (0, 0))
    screen.blit(big_title, (SCREEN_WIDTH/2 - (big_title.get_width()/2), SCREEN_HEIGHT/2 - 45))
    screen.blit(begin, (SCREEN_WIDTH / 2 - (begin.get_width() / 2), SCREEN_HEIGHT / 2 + 100))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                game_clock = RTL
                start_game = True
                for _ in range(NUM_BB):
                    HEIGHT_VARY = random.randint(WATER_HEIGHT, LOW_HEIGHT)
                    battleship.battleships.add(battleship.Battleship(random.randint(0, SCREEN_WIDTH), HEIGHT_VARY))
                # STARTS GAME
                # if vs. while
                while start_game:
                    if game_clock > 0:
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
                        screen.blit(time, (SCREEN_WIDTH - 540, 125))
                        screen.blit(title, (SCREEN_WIDTH - (title.get_width() + 10), 0))

                        for sunk_ship in sunk_ships:
                            print("I sunk a ship")
                            # sounds.explosion.play()

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
                    else:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit()
                        screen.blit(GO, (SCREEN_WIDTH / 2 - (GO.get_width() / 2), SCREEN_HEIGHT / 2 - 45))
                        SCORE = game_font_med.render(f"SCORE: {score}", True, (0, 0, 0))
                        screen.blit(SCORE, (SCREEN_WIDTH / 2 - (SCORE.get_width() / 2), SCREEN_HEIGHT / 2 + GO.get_height() / 2))
                        screen.blit(HIGH_SCORE, (SCREEN_WIDTH / 2 - (HIGH_SCORE.get_width() / 2), SCREEN_HEIGHT / 2 + GO.get_height() / 2 + SCORE.get_height()))
                        screen.blit(GO_BACK, (SCREEN_WIDTH / 2 - (GO_BACK.get_width() / 2), SCREEN_HEIGHT / 2 + GO.get_height() / 2 + SCORE.get_height() + HIGH_SCORE.get_height()))
                        pygame.display.flip()
