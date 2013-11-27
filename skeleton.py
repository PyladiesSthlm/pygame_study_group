# Docs at: http://www.pygame.org/docs/ref/index.html

import pygame
from sprite import *
from text import *

def main():
  # Initialize pygame and setup the window 
  pygame.init()
  screen = pygame.display.set_mode((500, 500))

  # Set a white background, same size as window
  background = pygame.Surface(screen.get_size())
  background.fill((250, 250, 250))

  # Create a text object at position 10, 10
  text = Text('Pyladies', (10, 10))

  # Create a sprite and add it to a list of sprites to render
  kitten = Sprite('kitten.jpg')
  allsprites = pygame.sprite.RenderPlain((kitten))

  running = True
  while running:
    # Handle input events from the user
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False

    kitten.update()

    screen.blit(background, (0, 0))
    screen.blit(text.surface, text.position)

    allsprites.draw(screen) 
    pygame.display.update()

  pygame.quit() 

if __name__ == '__main__':
  main()