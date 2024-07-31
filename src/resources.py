import pygame
import os

def load_image_with_path(file_name, scale_factor=1):
    # Ajuste o caminho para a pasta assets/images
    file_path = os.path.join('assets', 'images', file_name)
    
    try:
        image = pygame.image.load(file_path)
        if scale_factor != 1:
            width, height = image.get_size()
            image = pygame.transform.scale(image, (width * scale_factor, height * scale_factor))
        return image
    except pygame.error as e:
        print(f"Não foi possível carregar a imagem: {file_path}")
        print(e)
        raise
