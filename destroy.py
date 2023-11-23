import pygame
import random
pygame.init()
game_font_small = pygame.font.Font("assets/fonts/Wargate-Normal.ttf", 35)
hit = game_font_small.render("Hit +1", True, (0, 0, 0))


class Destroy(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = hit
        self.rect = pygame.rect.Rect(0, 0, self.image.get_width(), self.image.get_height())
        self.health = 90

    def update(self):
        self.health -= 1


destroys = pygame.sprite.Group()
