import pygame
import sys
from settings import *
from player import Player
from enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Invasión Espacial')
        self.clock = pygame.time.Clock()
        self.player = Player(self.screen)
        self.enemies = [Enemy(self.screen) for _ in range(5)]

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(BLACK)
            self.player.draw()
            for enemy in self.enemies:
                enemy.move()
                enemy.draw()

            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
