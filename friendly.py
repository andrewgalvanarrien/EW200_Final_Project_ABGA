import pygame
from settings import *
import random
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Friendly(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.right_image = pygame.image.load("assets/images/friendly1.png").convert()
        self.right_image.set_colorkey((0, 0, 0))
        self.right_image = pygame.transform.scale_by(self.right_image, y/650)
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.left_image.set_colorkey((0, 0, 0))
        self.image = self.right_image
        self.rect = pygame.rect.Rect.bottomleft
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving_left = random.random() > 0.5

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_left:
            self.rect.x -= FRIENDLY_SPEED
            self.image = self.left_image
        else:
            self.rect.x += FRIENDLY_SPEED
            self.image = self.right_image


friendlies = pygame.sprite.Group()
