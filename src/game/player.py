import pygame
from src.config import HEIGHT

class Player(pygame.sprite.Sprite):
    def __init__(self, run_images, jump_images, x, y, standing_image=None, floor_image=None):
        super().__init__()
        self.run_images = run_images
        self.jump_images = jump_images
        self.current_image = 0  # Adicione esta linha para inicializar current_image
        self.standing_image = standing_image
        self.image = standing_image if standing_image else run_images[0]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x = x
        self.y = y
        self.vel_y = 0
        self.is_jumping = False
        self.is_running = False
        self.facing_right = True
        self.floor_image = floor_image
        self.is_falling = False
        self.jump_timer = 0
        self.jumping_started = False
        self.cooldown = 0
        self.cooldown_duration = 10  # Tempo de cooldown em frames
        self.jump_speed = -20  # Aumenta a velocidade do pulo

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1
            # Durante o cooldown, o personagem fica parado e exibe o sprite de preparação
            if self.is_jumping:
                self.image = self.jump_images[0]
            else:
                self.image = self.standing_image
            # Inverte a imagem somente se o jogador está virado para a esquerda
            if not self.facing_right:
                self.image = pygame.transform.flip(self.image, True, False)
            self.rect.topleft = (self.x, self.y)  # Atualiza a posição da hitbox
            return

        if self.is_jumping:
            if not self.jumping_started:
                self.image = self.jump_images[0]
                self.jumping_started = True
            else:
                self.image = self.jump_images[1]

            self.vel_y += 1  # Gravidade
            self.y += self.vel_y

            # Verifique se o jogador deve parar de pular e ajustar a posição
            if self.y >= HEIGHT - self.rect.height:
                self.y = HEIGHT - self.rect.height
                self.is_jumping = False
                self.is_falling = False
                self.vel_y = 0
                self.jumping_started = False
                self.cooldown = self.cooldown_duration  # Inicia o cooldown ao tocar o chão
        else:
            if self.is_running:
                self.current_image += 0.2
                if self.current_image >= len(self.run_images):
                    self.current_image = 0
                self.image = self.run_images[int(self.current_image)]
            else:
                self.image = self.standing_image

        # Inverte a imagem somente se o jogador está virado para a esquerda e não está no cooldown
        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)

        # Atualiza a posição da hitbox com base na posição atual do personagem
        self.rect.topleft = (self.x, self.y)

    def jump(self):
        if not self.is_jumping and self.cooldown <= 0:
            self.vel_y = self.jump_speed  # Ajusta a velocidade do pulo
            self.is_jumping = True
            self.is_falling = True
            self.jumping_started = False
            self.jump_timer = 0
            self.cooldown = self.cooldown_duration  # Inicia o cooldown ao pular

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
