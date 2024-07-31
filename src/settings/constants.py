from pygame.surface import SurfaceType

class GlobalConstants:
  class screen:
    WIDTH: int = 1280
    HEIGHT: int = 720
    SURFACE: SurfaceType = (
      WIDTH, HEIGHT
    ) 
  
  class application:
    NAME: str = "Pixil Fight"
    VERSION: str = "1.0.0"  
    FPS: float = 60.0

  class paths:
    FONTS: str = "/assets/fonts/"
    SOUNDS: str = "/assets/sounds/"
    IMAGES: str = "/assets/images/"

