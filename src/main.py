import sys
import os
import pygame

# Adiciona o diretório 'src' ao PYTHONPATH
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from config import WIDTH, HEIGHT, BLACK, FPS
from resources import load_image_with_path
from menu_functions import show_menu
from settings_menu import show_settings_menu
from pause_menu import show_pause_menu
from audio import init_audio, load_music, play_music
from classes import Player
from game_functions import handle_input_player1, handle_input_player2

# Inicialize o Pygame e o áudio
pygame.init()
init_audio()  # Inicializa o mixer de áudio

# Carregar e tocar a música de fundo
background_music = load_music('Hub_Music.mp3')
play_music(background_music)

def load_images():
    try:
        player1_run_images = [load_image_with_path(f'player1_run{i}.png', scale_factor=2) for i in range(1, 4)]
        player1_standing_image = load_image_with_path('player1.png', scale_factor=2)
        player1_jump_images = [load_image_with_path(f'player1_jump{i}.png', scale_factor=2) for i in range(1, 3)]

        player2_run_images = [load_image_with_path(f'player2_run{i}.png', scale_factor=2) for i in range(1, 4)]
        player2_standing_image = load_image_with_path('player2.png', scale_factor=2)
        player2_jump_images = [load_image_with_path(f'player2_jump{i}.png', scale_factor=2) for i in range(1, 3)]

        background_image = load_image_with_path('Map_1.png', scale_factor=1)
        floor_image = load_image_with_path('Floor_1.png', scale_factor=1)

        if None in player1_run_images + [player1_standing_image] + player1_jump_images + \
                  player2_run_images + [player2_standing_image] + player2_jump_images:
            raise ValueError("Erro ao carregar uma ou mais imagens do jogador")

        return (player1_run_images, player1_standing_image, player1_jump_images,
                player2_run_images, player2_standing_image, player2_jump_images,
                background_image, floor_image)
    except Exception as e:
        print(f"Erro ao carregar imagens: {e}")
        pygame.quit()
        sys.exit()

def draw(screen, players, floor_image, floor_rect):
    """Desenha os jogadores e o chão na tela."""
    screen.blit(floor_image, floor_rect.topleft)
    for player in players:
        screen.blit(player.image, player.rect.topleft)

def start_game():
    # Configurar a tela
    global screen
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.Font(None, 36)

    # Carregar imagens
    (player1_run_images, player1_standing_image, player1_jump_images,
     player2_run_images, player2_standing_image, player2_jump_images,
     background_image, floor_image) = load_images()

    # Ajustar imagens
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    floor_image = pygame.transform.scale(floor_image, (WIDTH, floor_image.get_height()))

    # Configurar a hitbox do chão
    floor_hitbox_height = 50  # Ajuste conforme necessário
    floor_rect = pygame.Rect(0, HEIGHT - floor_hitbox_height, WIDTH, floor_hitbox_height)

    # Inicialização dos jogadores
    player1 = Player(player1_run_images, player1_jump_images, 100,
                     HEIGHT - player1_standing_image.get_height() - floor_hitbox_height,
                     standing_image=player1_standing_image)
    player2 = Player(player2_run_images, player2_jump_images, 200,
                     HEIGHT - player2_standing_image.get_height() - floor_hitbox_height,
                     standing_image=player2_standing_image)

    players = pygame.sprite.Group(player1, player2)
    # camera = Camera(WIDTH, HEIGHT)  # Comente a câmera por enquanto, se necessário

    # Configurações do jogo
    clock = pygame.time.Clock()
    running = True

    # Exibir o menu principal
    show_menu(screen, font, options=['Start Game', 'Settings', 'Quit'])

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    show_pause_menu(screen, font)
                elif event.key == pygame.K_s:
                    show_settings_menu(screen, font)

        # Lógica do jogo
        handle_input_player1(player1)
        handle_input_player2(player2)
        
        # Atualizar jogadores
        players.update()

        # Verifica se os jogadores colidem com o chão
        for player in players:
            if player.rect.bottom > floor_rect.top:
                player.rect.bottom = floor_rect.top
                player.is_jumping = False

        # Configuração da tela
        screen.fill(BLACK)
        screen.blit(background_image, (0, 0))

        # Desenhar o chão e os jogadores
        draw(screen, players, floor_image, floor_rect)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    start_game()
