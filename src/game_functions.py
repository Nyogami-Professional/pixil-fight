import pygame

def handle_input_player1(player1):
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a]:
        player1.x -= 5
        player1.is_running = True
        player1.facing_right = False
    elif keys[pygame.K_d]:
        player1.x += 5
        player1.is_running = True
        player1.facing_right = True
    else:
        player1.is_running = False

    if keys[pygame.K_SPACE] and not player1.is_jumping:
        player1.jump()

def handle_input_player2(player2):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player2.x -= 5
        player2.is_running = True
        player2.facing_right = False
    elif keys[pygame.K_RIGHT]:
        player2.x += 5
        player2.is_running = True
        player2.facing_right = True
    else:
        player2.is_running = False

    if keys[pygame.K_UP] and not player2.is_jumping:
        player2.jump()
