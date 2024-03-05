# Este archivo define la clase Enemy, que controla los enemigos del juego.

import pygame
import os
from random import randint

from InvasionEspacial.src.settings import SCREEN_WIDTH

class Enemy:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load(os.path.join('assets/images', 'enemy.png'))
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = randint(-150, -100)
        self.speed = randint(2, 6)

    def move(self):
        self.rect.y += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)
