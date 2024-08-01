import pygame
from config import WIDTH, HEIGHT, BLACK
import sys

def show_settings_menu(screen, font):
    # Criar botões
    return_button = pygame.Rect(WIDTH / 2 - 50, HEIGHT / 2 - 25, 100, 50)

    while True:
        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (0, 128, 0), return_button)

        return_text = font.render('Return', True, BLACK)

        screen.blit(return_text, (return_button.x + 10, return_button.y + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if return_button.collidepoint(event.pos):
                    return

        pygame.display.flip()
