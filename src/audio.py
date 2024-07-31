import pygame
import os

def load_music(music_path):
    try:
        pygame.mixer.init()
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)  # Reproduz em loop
        print("Música carregada com sucesso")
    except pygame.error as e:
        print(f"Erro ao carregar música: {e}")

if __name__ == "__main__":
    # Ajuste o caminho para o arquivo de música
    music_path = os.path.join(os.path.dirname(__file__), '..', 'assets', 'sounds', 'Fight_Music.mp3')
    load_music(music_path)

def init_audio():
    pygame.mixer.init()

def play_music(loop=False):
    pygame.mixer.music.play(-1 if loop else 0)

def stop_music():
    pygame.mixer.music.stop()
