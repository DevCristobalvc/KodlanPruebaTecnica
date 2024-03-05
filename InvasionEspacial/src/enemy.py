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
        # Carga la imagen
        image = pygame.image.load(image_path)

        # Decide el porcentaje del ancho de la pantalla que la imagen del enemigo debería ocupar
        target_width_percentage = 0.2  # 20% del ancho de la pantalla
        # Calcula el nuevo ancho y alto para mantener la relación de aspecto
        aspect_ratio = image.get_height() / image.get_width()
        target_width = int(SCREEN_WIDTH * target_width_percentage)
        target_height = int(target_width * aspect_ratio)

        # Redimensiona la imagen
        self.image = pygame.transform.scale(image, (target_width, target_height))
        self.rect = self.image.get_rect()

        # Ajusta la posición inicial del enemigo
        print(f"SCREEN_WIDTH: {SCREEN_WIDTH}, Enemy width: {self.rect.width}")
        self.rect.x = randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = randint(-150, -100)
        self.speed = randint(2, 6)

    def move(self):
        self.rect.y += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)
