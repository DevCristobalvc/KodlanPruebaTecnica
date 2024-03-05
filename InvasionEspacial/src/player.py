# Aquí definimos la clase Player que maneja la lógica del jugador, como dibujar la nave y moverla.

import pygame
import os

from settings import SCREEN_HEIGHT, SCREEN_WIDTH

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load(os.path.join('assets/images', 'player.png'))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10)
        self.speed = 5

    def move(self, direction):
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= self.speed
        elif direction == "right" and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)
