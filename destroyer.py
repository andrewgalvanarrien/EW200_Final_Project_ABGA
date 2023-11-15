import pygame
from settings import *


class Destroyer(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        # 1.) load image
        # 2.) scale the image based on the y
        # 3.) position the ship based on x,y
        #       create a rectangle based on the image
        #
        self.right_image = pygame.image.load("assets/images/destroyer.png").convert()
        self.right_image.set_colorkey((0, 0, 0))
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.left_image.set_colorkey((0, 0, 0))
        self.image = self.right_image

        self.rect = pygame.rect.Rect.bottomleft

        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())

        self.moving_left = True
        self.moving_right = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_left:
            self.rect.x -= D_SPEED
            self.image = self.left_image
        elif self.moving_right:
            self.rect.x += D_SPEED
            self.image = self.right_image


destroyers = pygame.sprite.Group()