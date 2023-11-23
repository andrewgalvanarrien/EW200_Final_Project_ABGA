import pygame
import friendly
import torpedo
from settings import *
import sys
import battleship
import random
import explosion
import destroy
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

# SCREEN & SOUND BTS
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Torpedo!")
background = pygame.image.load("assets/images/background.png").convert()
data_background = pygame.image.load("assets/images/data_background.png").convert()
explosion_sound = pygame.mixer.Sound("assets/sounds/explosion.wav")
splash_sound = pygame.mixer.Sound("assets/sounds/watersplash2.flac")

# RENDERS
title = game_font.render("Torpedo!", True, (0, 0, 0))
begin = game_font_small.render("Press 'ENTER' to Start", True, (0, 0, 0))
big_title = game_font_big.render("Torpedo!", True, (0, 0, 0))
GO = game_font_medbig.render("GAME OVER!", True, (0, 0, 0))
HIGH_SCORE = game_font_med.render(f"HIGH SCORE: {high_score}", True, (0, 0, 0))
GO_BACK = game_font_med.render("Press 'ENTER' to Return to Start", True, (0, 0, 0))
HIT = game_font_small.render("Hit +1", True, (0, 0, 0))


def increase_angle(angle):
    angle += .1
    return angle


def decrease_angle(angle):
    angle -= .1
    return angle


def explosion1(x, y):
    the_explosion = explosion.Explosion(x, y)
    the_explosion.draw(screen, x, y)


# THE GAME
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
                splash_sound.play()
                game_clock = RTL  # sets round limit timer; immediately begins countdown
                start_game = True
                for _ in range(NUM_BB):
                    HEIGHT_VARY = random.randint(WATER_HEIGHT, LOW_HEIGHT)
                    battleship.battleships.add(battleship.Battleship(random.randint(0, SCREEN_WIDTH), HEIGHT_VARY))
                for _ in range(NUM_FR):
                    HEIGHT_VARY = random.randint(WATER_HEIGHT, LOW_HEIGHT)
                    friendly.friendlies.add(friendly.Friendly(random.randint(0, SCREEN_WIDTH), HEIGHT_VARY))

                # STARTS GAME
                while start_game:
                    if game_clock > 0:
                        rotating_left = False
                        rotating_right = False
                        # Listening for keyboard
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

                        # Removal of Sprites via bounds:
                        for fired_torpedo in list(torpedo.torpedoes):
                            if fired_torpedo.rect.top <= T_WATER_HEIGHT or fired_torpedo.rect.x <= -84 or fired_torpedo.rect.x >= SCREEN_WIDTH:
                                torpedo.torpedoes.remove(fired_torpedo)

                        for missed_bship in battleship.battleships:
                            if missed_bship.rect.x <= -239 or missed_bship.rect.x >= SCREEN_WIDTH:
                                HEIGHT_VARY = random.randint(WATER_HEIGHT, LOW_HEIGHT)
                                battleship.battleships.remove(missed_bship)
                                battleship.battleships.add(battleship.Battleship(-238 + ((random.randint(0, 1)) * (SCREEN_WIDTH + 238)), HEIGHT_VARY))

                        for missed_fship in friendly.friendlies:
                            if missed_fship.rect.x <= -246 or missed_fship.rect.x >= SCREEN_WIDTH:
                                HEIGHT_VARY = random.randint(WATER_HEIGHT, LOW_HEIGHT)
                                friendly.friendlies.remove(missed_fship)
                                friendly.friendlies.add(friendly.Friendly(-245 + ((random.randint(0, 1)) * (SCREEN_WIDTH + 245)), HEIGHT_VARY))

                        # Removal of Sprites via collision:
                        sunk_bships = pygame.sprite.groupcollide(torpedo.torpedoes, battleship.battleships, True,True)
                        for sunk_ship in sunk_bships:
                            HEIGHT_VARY = random.randint(WATER_HEIGHT, LOW_HEIGHT)
                            explosion_sound.play()
                            #destroy.destroys.add(sunk_ship.rect.x, sunk_ship.rect.y)
                            #for hit in list(destroy.destroys):
                                #if hit.health == 0:
                                    #destroy.destroys.remove(hit)
                            #explosion1(sunk_ship.rect.x, sunk_ship.rect.y)
                            #screen.blit(HIT, (sunk_ship.rect.x, sunk_ship.rect.y - 100))
                            #(sunk_ship.rect.x, sunk_ship.rect.y)
                            #(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)s
                            battleship.battleships.add(battleship.Battleship(-238 + ((random.randint(0, 1)) * (SCREEN_WIDTH + 238)), HEIGHT_VARY))

                        sunk_fships = pygame.sprite.groupcollide(torpedo.torpedoes, friendly.friendlies, True, True)
                        for sunk_ship in sunk_fships:
                            HEIGHT_VARY = random.randint(WATER_HEIGHT, LOW_HEIGHT)
                            explosion_sound.play()
                            friendly.friendlies.add(friendly.Friendly(-245 + ((random.randint(0, 1)) * (SCREEN_WIDTH + 245)), HEIGHT_VARY))

                        if rotating_left:
                            angle += 0.1
                        elif rotating_right:
                            angle -= 0.1

                        # Score keeping variables:
                        score += len(sunk_bships)
                        score -= len(sunk_fships)

                        # Score board application:
                        screen.blit(background, (0, 0))
                        scoreboard = game_font.render(f"Score: {score}", True, (0, 0, 0))
                        time = game_font.render(f"Time Left: {game_clock}", True, (0, 0, 0))
                        screen.blit(scoreboard, (SCREEN_WIDTH - (title.get_width() + 10), 60))
                        screen.blit(time, (SCREEN_WIDTH - 540, 125))
                        screen.blit(title, (SCREEN_WIDTH - (title.get_width() + 10), 0))

                        # All class function calls + timekeeping
                        torpedo.torpedoes.update()
                        destroy.destroys.update()
                        friendly.friendlies.update()
                        battleship.battleships.update()
                        torpedo.torpedoes.draw(screen)
                        destroy.destroys.draw(screen)
                        battleship.battleships.draw(screen)
                        friendly.friendlies.draw(screen)
                        pygame.display.flip()
                        clock.tick(60)
                        game_clock -= 1/60

                    else:
                        # GAME OVER SCREEN
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
