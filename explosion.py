import pygame


class Explosion:

    def __init__(self, x, y):
        self.image = pygame.image.load("assets/images/explosion.gif").convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = pygame.rect.Rect(0, 0, self.image.get_width(), self.image.get_height())

    def draw(self, screen, x, y ):
        screen.blit(self.image, screen, x, y)


