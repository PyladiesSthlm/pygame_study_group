import pygame

from sprite import *
from wikipedia_sprite import *
from text import *

WHITE = (250, 250, 250)
BLACK = (0, 0, 0)

def main():
  # Initialize pygame and setup the window 
  pygame.init()
  screen = pygame.display.set_mode((500, 500))

  # Set a white background, same size as window
  background = pygame.Surface(screen.get_size())
  background.fill(WHITE)

  # Create a text object at position 10, 10
  text = Text('Pyladies!', (10, 10))

  # Create a sprite from a local image 
  kitten = Sprite('kitten.jpg')

  # Download an image from wikipedia and create a sprite from it 
  tom_hanks = WikipediaSprite('Tom Hanks')

  # Create a group with the sprites to draw together
  allsprites = pygame.sprite.LayeredUpdates((tom_hanks, kitten))

  clock = pygame.time.Clock()
  running = True

  while running:

    # Limit the while loop to a max of 20 times per second.
    clock.tick(20)

    # Handle input events from the user
    for event in pygame.event.get():
      
      if event.type == pygame.MOUSEBUTTONDOWN:
        for sprite in allsprites.get_sprites_at(event.pos):
          sprite.being_dragged = True

      elif event.type == pygame.MOUSEBUTTONUP:
        for sprite in allsprites.sprites():
          sprite.being_dragged = False

      if event.type == pygame.QUIT:
          running = False

    # Draw background and text
    screen.blit(background, (0, 0))
    screen.blit(text.surface, text.position)

    # Draw a solid rectangle
    pygame.draw.rect(screen, BLACK, [0, 460, 180, 40])

    # Update and render sprites
    allsprites.update()
    allsprites.draw(screen) 

    pygame.display.update()

  pygame.quit() 

if __name__ == '__main__':
  main()