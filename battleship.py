import pygame
from settings import *
import random
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Battleship(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.right_image = pygame.image.load("assets/images/battleship1.png").convert()
        self.right_image.set_colorkey((0, 0, 0))
        self.right_image = pygame.transform.scale_by(self.right_image, .5)
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.left_image.set_colorkey((0, 0, 0))
        self.image = self.right_image
        self.rect = pygame.rect.Rect.bottomleft
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_left = random.random()>0.5
        # if moving left

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_left:
            self.rect.x -= BSHIP_SPEED
            self.image = self.left_image
        else:
            self.rect.x += BSHIP_SPEED
            self.image = self.right_image


battleships = pygame.sprite.Group()
