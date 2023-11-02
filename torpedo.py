import pygame
from settings import *
import math

class Torpedo(pygame.sprite.Sprite):

    def __init__(self, angle=0, x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT):
        super().__init__()
        self.image = pygame.image.load("assets/images/rd.png").convert()
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        self.moving = True
        self.angle = angle

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.moving:
            self.rect.x += TORPEDO_SPEED*math.cos(self.angle)
            self.rect.y += TORPEDO_SPEED*math.sin(self.angle)

