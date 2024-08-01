import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, run_images, jump_images, x, y, standing_image=None):
        super().__init__()
        self.run_images = run_images
        self.jump_images = jump_images
        self.standing_image = standing_image
        self.image = standing_image if standing_image else run_images[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 5
        self.jump_speed = -15
        self.gravity = 1
        self.velocity_y = 0
        self.on_ground = False
        self.direction = 1  # 1 para direita, -1 para esquerda

    def update(self):
        self.apply_gravity()
        self.rect.x += self.speed * self.direction
        self.rect.y += self.velocity_y

    def apply_gravity(self):
        if not self.on_ground:
            self.velocity_y += self.gravity
        else:
            self.velocity_y = 0

    def jump(self):
        if self.on_ground:
            self.velocity_y = self.jump_speed
            self.on_ground = False

    def move_left(self):
        self.direction = -1

    def move_right(self):
        self.direction = 1

    def stop(self):
        self.speed = 0
