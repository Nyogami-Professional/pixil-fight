import pygame

class PyGameWrapper:
  def __init__(self, name: str):
    self.name = name

  def init():
    try:
      pygame.init()

    except pygame.error as e:
      print(f"Failed to initialize Pygame: {e}")
      return False
    finally:
      Exception("Failed to initialize Pygame")