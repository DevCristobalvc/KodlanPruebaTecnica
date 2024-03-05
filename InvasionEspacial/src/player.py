# Aquí definimos la clase Player que maneja la lógica del jugador, como dibujar la nave y moverla.

import pygame
import os

from settings import SCREEN_HEIGHT, SCREEN_WIDTH

class Player:
    def __init__(self, screen):
        self.screen = screen
        current_path = os.path.dirname(__file__)  # Ruta del directorio de player.py
        image_path = os.path.join(current_path, '../assets/images', 'player.png')
        
        # Carga la imagen original
        original_image = pygame.image.load(image_path)
        
        # Decide el porcentaje del ancho de la pantalla que la imagen del jugador debería ocupar
        target_width_percentage = 0.15  # Ejemplo: 15% del ancho de la pantalla
        target_width = int(SCREEN_WIDTH * target_width_percentage)
        
        # Mantiene la relación de aspecto de la imagen original
        aspect_ratio = original_image.get_height() / original_image.get_width()
        target_height = int(target_width * aspect_ratio)
        
        # Redimensiona la imagen a las nuevas dimensiones
        self.image = pygame.transform.scale(original_image, (target_width, target_height))
        self.rect = self.image.get_rect()
        
        # Ajusta la posición inicial del jugador en el centro abajo de la pantalla
        self.rect.midbottom = (SCREEN_WIDTH / 2, SCREEN_HEIGHT - 10)
        
        self.speed = 5

    def move(self, direction):
        if direction == "left" and self.rect.left > 0:
            self.rect.x -= self.speed
        elif direction == "right" and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)
