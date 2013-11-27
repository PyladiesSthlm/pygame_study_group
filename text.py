import pygame

class Text(pygame.surface.Surface):
  def __init__(self, string, position):
    self.position = position

    font = pygame.font.SysFont("monospace", 65)
    self.surface = font.render(string, 1, (0, 0, 0))