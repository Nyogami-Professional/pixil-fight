import pygame
import os

def init_audio():
    """Inicializa o mixer de áudio do Pygame."""
    pygame.mixer.init()

def load_music(music_path):
    """Carrega um arquivo de música."""
    try:
        pygame.mixer.music.load(music_path)
        print("Música carregada com sucesso")
        return music_path  # Retorna o caminho da música carregada
    except pygame.error as e:
        print(f"Erro ao carregar música: {e}")
        return None

def play_music(music_file, loop=False):
    """Reproduz um arquivo de música."""
    if music_file:
        pygame.mixer.music.load(music_file)
        pygame.mixer.music.play(-1 if loop else 0)
    else:
        print("Nenhum arquivo de música carregado.")

def stop_music():
    """Para a reprodução da música."""
    pygame.mixer.music.stop()

if __name__ == "__main__":
    # Ajuste o caminho para o arquivo de música
    music_path = os.path.join(os.path.dirname(__file__), '..', 'assents', 'music', 'Fight_Music.mp3')
    music_file = load_music(music_path)
    play_music(music_file)
