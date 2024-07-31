import pygame
import sys  # Adicione esta linha para importar o módulo sys
from src.config import WIDTH, HEIGHT, BLACK

def show_pause_menu(screen, font):
    # Criar botões
    resume_button = pygame.Rect(WIDTH / 2 - 50, HEIGHT / 2 - 25, 100, 50)
    settings_button = pygame.Rect(WIDTH / 2 - 50, HEIGHT / 2 + 35, 100, 50)
    menu_button = pygame.Rect(WIDTH / 2 - 50, HEIGHT / 2 + 105, 100, 50)

    while True:
        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, (0, 128, 0), resume_button)
        pygame.draw.rect(screen, (0, 128, 0), settings_button)
        pygame.draw.rect(screen, (128, 0, 0), menu_button)

        resume_text = font.render('Resume', True, BLACK)
        settings_text = font.render('Settings', True, BLACK)
        menu_text = font.render('Menu', True, BLACK)

        screen.blit(resume_text, (resume_button.x + 10, resume_button.y + 10))
        screen.blit(settings_text, (settings_button.x + 10, settings_button.y + 10))
        screen.blit(menu_text, (menu_button.x + 10, menu_button.y + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  # Agora funciona corretamente
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if resume_button.collidepoint(event.pos):
                    return 'resume'
                elif settings_button.collidepoint(event.pos):
                    return 'settings'
                elif menu_button.collidepoint(event.pos):
                    return 'menu'

        pygame.display.flip()
