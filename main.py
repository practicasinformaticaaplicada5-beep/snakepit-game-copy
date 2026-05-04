# main.py
import pygame
import sys
from settings import *
from snake import Snake
from food import Food

def main():
    # Inicializar Pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Juego de la Serpiente')
    clock = pygame.time.Clock()

    # Instanciar objetos
    snake = Snake()
    food = Food()
    score = 0

    # Fuente para el texto
    font = pygame.font.SysFont("bahnschrift", 25)

    # Bucle principal del juego
    while True:
        # 1. Manejo de eventos (Teclado)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction("RIGHT")

        # 2. Lógica del juego
        snake.move()

        # Comprobar si la serpiente come
        if snake.body[0] == food.position:
            snake.grow = True
            food.randomize_position()
            score += 1

        # Comprobar si pierde
        if snake.check_collision():
            screen.fill(BLACK)
            msg = font.render(f"¡Game Over! Puntuación final: {score}", True, RED)
            # Centrar mensaje
            msg_rect = msg.get_rect(center=(WIDTH/2, HEIGHT/2))
            screen.blit(msg, msg_rect)
            pygame.display.flip()
            
            pygame.time.wait(3000) # Espera 3 segundos
            pygame.quit()
            sys.exit()

        # 3. Dibujar en pantalla
        screen.fill(BLACK) # Limpiar pantalla
        snake.draw(screen)
        food.draw(screen)

        # Mostrar puntuación
        score_text = font.render(f"Puntuación: {score}", True, WHITE)
        screen.blit(score_text, [10, 10])

        pygame.display.flip() # Actualizar pantalla
        
        # 4. Controlar los FPS
        clock.tick(FPS)

if __name__ == "__main__":
    main()