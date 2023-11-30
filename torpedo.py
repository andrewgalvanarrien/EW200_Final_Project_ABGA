import pygame
from settings import *
import math


class Torpedo(pygame.sprite.Sprite):

    def __init__(self, angle):
        super().__init__()
        self.image = pygame.image.load("assets/images/torpedo.png").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.rect.Rect(0, 0, self.image.get_width(), self.image.get_height())
        self.rect.midbottom = (SCREEN_WIDTH/2, SCREEN_HEIGHT)
        self.moving = True
        self.angle = angle
        self.rotating_left = False
        self.rotating_right = False

    def update(self):
        if self.moving:
            self.rect.x += TORPEDO_SPEED * math.cos(self.angle)
            self.rect.y += - (TORPEDO_SPEED * math.sin(self.angle))
            new_position = self.rect.center

    def targeting(self):
        if self.rotating_left == True:
            self.angle += 0.1
        if self.rotating_right == True:
            self.angle += 0.1


torpedoes = pygame.sprite.Group()
