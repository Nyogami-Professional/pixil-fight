import os
import pygame
import sys
import audio
from src.config import WIDTH, HEIGHT, BLACK

base_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Diretório base: {base_dir}")

def show_menu(screen, font, options):
    # Ajuste o caminho para a imagem do menu
    hub_image_path = os.path.join(base_dir, '..', 'assets', 'images', 'Hub_image.png')
    hub_image = pygame.image.load(hub_image_path)
    hub_image = pygame.transform.scale(hub_image, (WIDTH, HEIGHT))

    # Tocar a música do hub
    audio.stop_music()
    hub_music_path = os.path.join(base_dir, '..', 'assets', 'music', 'Hub_Music.mp3')
    audio.load_music(hub_music_path)
    audio.play_music(loop=True)

    # Criar botões
    start_button = pygame.Rect(WIDTH / 2 - 50, HEIGHT / 2 - 25, 100, 50)
    settings_button = pygame.Rect(WIDTH / 2 - 50, HEIGHT / 2 + 35, 170, 50)
    exit_button = pygame.Rect(WIDTH / 2 - 50, HEIGHT / 2 + 105, 100, 50)
    
    while True:
        screen.blit(hub_image, (0, 0))

        pygame.draw.rect(screen, (0, 128, 0), start_button)
        pygame.draw.rect(screen, (0, 128, 0), settings_button)
        pygame.draw.rect(screen, (128, 0, 0), exit_button)

        start_text = font.render('Start', True, BLACK)
        settings_text = font.render('Settings', True, BLACK)
        exit_text = font.render('Exit', True, BLACK)

        screen.blit(start_text, (start_button.x + 10, start_button.y + 10))
        screen.blit(settings_text, (settings_button.x + 10, settings_button.y + 10))
        screen.blit(exit_text, (exit_button.x + 10, exit_button.y + 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    return 'start'
                elif settings_button.collidepoint(event.pos):
                    return 'settings'
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
