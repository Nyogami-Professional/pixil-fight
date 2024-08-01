import pygame
import math
from config import HEIGHT  # Certifique-se de que o caminho está correto

# Inicialização do Pygame
pygame.init()

# Configuração da tela
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Jogo de Luta")

class Player(pygame.sprite.Sprite):
    def __init__(self, run_images, jump_images, x, y, standing_image=None):
        super().__init__()
        self.run_images = run_images
        self.jump_images = jump_images
        self.current_image = 0
        self.standing_image = standing_image
        self.image = self.standing_image if self.standing_image else self.run_images[0]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.x = x
        self.y = y
        self.vel_y = 0
        self.is_jumping = False
        self.is_running = False
        self.facing_right = True
        self.is_falling = False
        self.jump_timer = 0
        self.jumping_started = False
        self.cooldown = 0
        self.cooldown_duration = 10  # Tempo de cooldown em frames
        self.jump_speed = -20  # Velocidade do pulo
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self):
        if self.cooldown > 0:
            self.cooldown -= 1
            if self.is_jumping:
                self.image = self.jump_images[0]
                if not self.facing_right:
                    self.image = pygame.transform.flip(self.image, True, False)
            self.rect.topleft = (self.x, self.y)
            return

        if self.is_jumping:
            if not self.jumping_started:
                self.image = self.jump_images[0]
                if not self.facing_right:
                    self.image = pygame.transform.flip(self.image, True, False)
                self.jumping_started = True
            else:
                self.image = self.jump_images[1]
                if not self.facing_right:
                    self.image = pygame.transform.flip(self.image, True, False)

            self.vel_y += 1  # Gravidade
            self.y += self.vel_y

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

        if not self.facing_right and self.cooldown <= 0:
            self.image = pygame.transform.flip(self.image, True, False)

        if self.x < 0:
            self.x = 0
        if self.x > self.screen_width - self.rect.width:
            self.x = self.screen_width - self.rect.width
        if self.y < 0:
            self.y = 0
        if self.y > self.screen_height - self.rect.height:
            self.y = self.screen_height - self.rect.height

        self.rect.topleft = (self.x, self.y)

    def jump(self):
        if not self.is_jumping and self.cooldown <= 0:
            self.vel_y = self.jump_speed
            self.is_jumping = True
            self.is_falling = True
            self.jumping_started = False
            self.jump_timer = 0
            self.cooldown = self.cooldown_duration

    def draw(self, surface):
        if self.image:  # Adiciona uma verificação para garantir que a imagem não seja None
            surface.blit(self.image, (self.x, self.y))

class Camera:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.zoom = 1.0

    def update(self, player1, player2):
        distance = math.sqrt((player2.x - player1.x) ** 2 + (player2.y - player1.y) ** 2)
        self.zoom = max(1.0, min(2.0, 200 / distance))

        center_x = (player1.x + player2.x) / 2
        center_y = (player1.y + player2.y) / 2

        return center_x, center_y, self.zoom

    def apply(self, rect):
        return pygame.Rect(
            (rect.x - (self.screen_width / 2)) * self.zoom + (self.screen_width / 2),
            (rect.y - (self.screen_height / 2)) * self.zoom + (self.screen_height / 2),
            rect.width * self.zoom,
            rect.height * self.zoom
        )

def draw(screen, camera, players):
    for player in players:
        adjusted_rect = camera.apply(player.rect)
        screen.blit(pygame.transform.scale(player.image, (adjusted_rect.width, adjusted_rect.height)), adjusted_rect.topleft)

# Exemplo de uso no loop principal
# Substitua com suas imagens de jogador
player1_run_images = [pygame.Surface((50, 50)) for _ in range(3)]
player1_jump_images = [pygame.Surface((50, 50)) for _ in range(2)]
player2_run_images = [pygame.Surface((50, 50)) for _ in range(3)]
player2_jump_images = [pygame.Surface((50, 50)) for _ in range(2)]

# Verificação de carregamento de imagens
def check_images(images):
    for i, img in enumerate(images):
        if img is None:
            print(f"Erro: Imagem {i} não carregada corretamente.")
            return False
    return True

if not check_images(player1_run_images) or not check_images(player1_jump_images) or not check_images(player2_run_images) or not check_images(player2_jump_images):
    print("Erro: Um ou mais recursos de imagem não foram carregados corretamente.")
    pygame.quit()
    exit()

player1_standing_image = player1_run_images[0]  # Supondo que a imagem de pé é a primeira imagem de corrida
player2_standing_image = player2_run_images[0]

floor_hitbox_height = 10  # Defina isso de acordo com sua necessidade

player1 = Player(player1_run_images, player1_jump_images, 100, HEIGHT - player1_standing_image.get_height() - floor_hitbox_height + 10, standing_image=player1_standing_image)
player2 = Player(player2_run_images, player2_jump_images, 300, HEIGHT - player2_standing_image.get_height() - floor_hitbox_height + 10, standing_image=player2_standing_image)

camera = Camera(screen_width, screen_height)
players = [player1, player2]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Outras atualizações e lógica do jogo
    player1.update()
    player2.update()
    
    # Atualizar a câmera
    center_x, center_y, zoom = camera.update(player1, player2)
    
    # Desenhar os jogadores com a câmera aplicada
    screen.fill((0, 0, 0))  # Preenche a tela com preto antes de desenhar
    draw(screen, camera, players)

    # Atualizar a tela
    pygame.display.flip()

pygame.quit()
