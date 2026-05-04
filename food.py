# food.py
import pygame
import random
from settings import *

class Food:
    def __init__(self):
        self.position = [0, 0]
        self.randomize_position()

    def randomize_position(self):
        # Genera coordenadas aleatorias alineadas a la cuadrícula
        self.position[0] = random.randrange(0, WIDTH, BLOCK_SIZE)
        self.position[1] = random.randrange(0, HEIGHT, BLOCK_SIZE)

    def draw(self, surface):
        pygame.draw.rect(surface, RED, pygame.Rect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))