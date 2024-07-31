import sys
import os
import pygame

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
print("Diretório atual de trabalho:", os.getcwd())

from src.config import WIDTH, HEIGHT, BLACK, FPS
from src.resources import load_image_with_path
from src.menu_functions import show_menu
from src.settings_menu import show_settings_menu
from src.pause_menu import show_pause_menu
from src.audio import init_audio, load_music, play_music
from src.classes import Player
from src.game_functions import handle_input_player1, handle_input_player2

# Inicialize o Pygame e o áudio
pygame.init()
init_audio()  # Inicializa o mixer de áudio

# Carregue os recursos para os jogadores
player1_run_images = [load_image_with_path(f'player1_run{i}.png', scale_factor=2) for i in range(1, 4)]
player1_standing_image = load_image_with_path('player1.png', scale_factor=2)
player1_jump_images = [load_image_with_path(f'player1_jump{i}.png', scale_factor=2) for i in range(1, 3)]  # Imagens de pulo

player2_run_images = [load_image_with_path(f'player2_run{i}.png', scale_factor=2) for i in range(1, 4)]
player2_standing_image = load_image_with_path('player2.png', scale_factor=2)
player2_jump_images = [load_image_with_path(f'player2_jump{i}.png', scale_factor=2) for i in range(1, 3)]  # Imagens de pulo

def start_game():
    # Troca a música para a música de luta
    music_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'music', 'Fight_Music.mp3')
    load_music(music_path)
    play_music(loop=True)
    ...

    # Carregar a imagem de fundo e o piso
    background_image = load_image_with_path('Map_1.png', scale_factor=1)
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    floor_image = load_image_with_path('Floor_1.png', scale_factor=1)
    floor_image = pygame.transform.scale(floor_image, (WIDTH, floor_image.get_height()))

    # Ajustar a altura da hitbox do chão apenas para baixo
    floor_hitbox_height = 50
    floor_rect = pygame.Rect(0, HEIGHT - floor_hitbox_height, WIDTH, floor_hitbox_height)

    # Ajustar a posição inicial dos jogadores para não nascerem dentro do chão
    player1 = Player(player1_run_images, player1_jump_images, 100, HEIGHT - player1_standing_image.get_height() - floor_hitbox_height + 10, standing_image=player1_standing_image, floor_image=floor_image)
    player2 = Player(player2_run_images, player2_jump_images, 200, HEIGHT - player2_standing_image.get_height() - floor_hitbox_height + 10, standing_image=player2_standing_image, floor_image=floor_image)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Atualize as posições dos jogadores
        handle_input_player1(player1)
        handle_input_player2(player2)

        # Verifique se a tecla ESC foi pressionada
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            choice = show_pause_menu(screen, pygame.font.SysFont(None, 55))
            if choice == 'resume':
                continue
            elif choice == 'settings':
                show_settings_menu(screen, pygame.font.SysFont(None, 55))
            elif choice == 'menu':
                return  # Volta ao menu principal

        # Atualize o estado dos jogadores
        player1.update()
        player2.update()

        # Verifique a colisão com o chão
        if player1.rect.bottom > HEIGHT - floor_hitbox_height:
            player1.y = HEIGHT - floor_hitbox_height - player1.rect.height
            player1.vel_y = 0
            player1.is_jumping = False

        if player2.rect.bottom > HEIGHT - floor_hitbox_height:
            player2.y = HEIGHT - floor_hitbox_height - player2.rect.height
            player2.vel_y = 0
            player2.is_jumping = False

        # Atualize a tela com a imagem de fundo e o piso
        screen.blit(background_image, (0, 0))
        screen.blit(floor_image, (0, HEIGHT - floor_image.get_height()))

        # Desenhe os jogadores
        player1.draw(screen)
        player2.draw(screen)

        pygame.display.flip()

        # Controle de FPS
        clock.tick(FPS)

def main():
    font = pygame.font.SysFont(None, 55)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Inicialize o display aqui
    while True:
        choice = show_menu(screen, font, ['Start', 'Settings'])
        if choice == 'start':
            start_game()
        elif choice == 'settings':
            show_settings_menu(screen, font)
        elif choice == 'exit':
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()
