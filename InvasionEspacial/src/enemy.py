# Este archivo define la clase Enemy, que controla los enemigos del juego.

import pygame
import os
from random import randint

from settings import SCREEN_WIDTH

class Enemy:
    def __init__(self, screen):
        self.screen = screen
        # Obtiene la ruta del directorio actual donde se encuentra este script
        current_path = os.path.dirname(__file__)  # Ruta del directorio de enemy.py
        # Construye la ruta hacia la carpeta de assets
        image_path = os.path.join(current_path, '../assets/images', 'enemy.png')
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        # Ajusta la posición inicial del enemigo
        self.rect.x = randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = randint(-150, -100)
        self.speed = randint(2, 6)

    def move(self):
        self.rect.y += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)
