import pygame
from settings import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Battleship(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.right_image = pygame.image.load("assets/images/battleship1.png").convert()
        self.right_image.set_colorkey((0, 0, 0))
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.left_image.set_colorkey((0, 0, 0))
        self.image = self.right_image
        self.rect = pygame.rect.Rect.bottomleft
        self.rect = pygame.rect.Rect(x, y, self.image.get_width(), self.image.get_height())
        #self.rect = pygame.transform.scale_by(screen, .5)
        self.moving_left = False
        self.moving_right = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_left:
            self.rect.x -= BSHIP_SPEED
            self.image = self.left_image
        elif self.moving_right:
            self.rect.x += BSHIP_SPEED
            self.image = self.right_image
        #if self.rect.left < 0:
            #self.rect.left = 0
        #if self.rect.right > SCREEN_WIDTH:
            #self.rect.right = SCREEN_WIDTH

battleships = pygame.sprite.Group()
