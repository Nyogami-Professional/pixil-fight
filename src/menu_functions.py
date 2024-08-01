import os
import pygame
import sys
import audio
from config import WIDTH, HEIGHT, BLACK

base_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Diretório base: {base_dir}")

def show_menu(screen, font, options):
    # Ajuste o caminho para a imagem do menu
    hub_image_path = os.path.join(base_dir, '..', 'assents', 'images', 'Hub_image.png')
    hub_image = pygame.image.load(hub_image_path)
    hub_image = pygame.transform.scale(hub_image, (WIDTH, HEIGHT))

    # Tocar a música do hub
    audio.stop_music()
    hub_music_path = os.path.join(base_dir, '..', 'assents', 'music', 'Hub_Music.mp3')
    audio.load_music(hub_music_path)
    audio.play_music(hub_music_path, loop=True)

    # Criar botões
    button_width = 200
    button_height = 50
    start_button = pygame.Rect(WIDTH / 2 - button_width / 2, HEIGHT / 2 - button_height / 2 - 40, button_width, button_height)
    settings_button = pygame.Rect(WIDTH / 2 - button_width / 2, HEIGHT / 2 - button_height / 2 + 40, button_width, button_height)
    exit_button = pygame.Rect(WIDTH / 2 - button_width / 2, HEIGHT / 2 - button_height / 2 + 120, button_width, button_height)
    
    while True:
        screen.blit(hub_image, (0, 0))

        pygame.draw.rect(screen, (0, 128, 0), start_button)
        pygame.draw.rect(screen, (0, 128, 0), settings_button)
        pygame.draw.rect(screen, (128, 0, 0), exit_button)

        start_text = font.render('Start Game', True, BLACK)
        settings_text = font.render('Settings', True, BLACK)
        exit_text = font.render('Quit', True, BLACK)

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
