import pygame
from settings import *
import sys
pygame.init()
score = 0
high_score = 0

game_font_medbig = pygame.font.Font("assets/fonts/Wargate-Normal.ttf", 130)
game_font_med = pygame.font.Font("assets/fonts/Wargate-Normal.ttf", 55)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Torpedo!")
background = pygame.image.load("assets/images/background.png").convert()
GO = game_font_medbig.render("GAME OVER!", True, (0, 0, 0))
SCORE = game_font_med.render(f"SCORE: {score}", True, (0, 0, 0))
HIGH_SCORE = game_font_med.render(f"HIGH SCORE: {high_score}", True, (0, 0, 0))
GO_BACK = game_font_med.render("Press 'ENTER' to Return to Start", True, (0, 0, 0))
background.blit(GO, (SCREEN_WIDTH/2 - (GO.get_width()/2), SCREEN_HEIGHT/2 - 45))
background.blit(SCORE, (SCREEN_WIDTH/2 - (SCORE.get_width()/2), SCREEN_HEIGHT/2 + GO.get_height()/2))
background.blit(HIGH_SCORE, (SCREEN_WIDTH/2 - (HIGH_SCORE.get_width()/2), SCREEN_HEIGHT/2 + GO.get_height()/2 + SCORE.get_height()))
background.blit(GO_BACK, (SCREEN_WIDTH/2 - (GO_BACK.get_width()/2), SCREEN_HEIGHT/2 + GO.get_height()/2 + SCORE.get_height() + HIGH_SCORE.get_height()))

while True:
    screen.blit(background, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()