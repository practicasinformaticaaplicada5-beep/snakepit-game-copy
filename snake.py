# snake.py
import pygame
from settings import *

class Snake:
    def __init__(self):
        # La serpiente empieza en el centro
        self.body = [[WIDTH // 2, HEIGHT // 2]]
        self.direction = "RIGHT"
        self.grow = False

    def change_direction(self, dir):
        # Evita que la serpiente dé marcha atrás sobre sí misma
        if dir == "UP" and self.direction != "DOWN":
            self.direction = "UP"
        if dir == "DOWN" and self.direction != "UP":
            self.direction = "DOWN"
        if dir == "LEFT" and self.direction != "RIGHT":
            self.direction = "LEFT"
        if dir == "RIGHT" and self.direction != "LEFT":
            self.direction = "RIGHT"

    def move(self):
        head_x, head_y = self.body[0]

        if self.direction == "UP":
            head_y -= BLOCK_SIZE
        elif self.direction == "DOWN":
            head_y += BLOCK_SIZE
        elif self.direction == "LEFT":
            head_x -= BLOCK_SIZE
        elif self.direction == "RIGHT":
            head_x += BLOCK_SIZE

        # Insertar nueva cabeza
        self.body.insert(0, [head_x, head_y])

        # Si no ha comido, eliminamos la cola para simular movimiento
        if self.grow:
            self.grow = False
        else:
            self.body.pop()

    def check_collision(self):
        head_x, head_y = self.body[0]
        
        # Colisión con los bordes de la pantalla
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            return True
        
        # Colisión con su propio cuerpo
        if [head_x, head_y] in self.body[1:]:
            return True
            
        return False

    def draw(self, surface):
        for segment in self.body:
            pygame.draw.rect(surface, YELLOW, pygame.Rect(segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))