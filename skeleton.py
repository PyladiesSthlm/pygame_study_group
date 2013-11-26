# Docs at: http://www.pygame.org/docs/ref/index.html

import pygame, os

class Kitten(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self) #call Sprite intializer
    self.image = load_image('kitten.jpg')
    self.rect = self.image.get_rect()
    self.rect.center = (250, 250)

  def update(self):
    self.rect.topleft = pygame.mouse.get_pos()

def load_image(imageName):
  fullPath = os.path.join("images", imageName)

  try:
    image = pygame.image.load(fullPath)
    if image.get_alpha() is None:
      image = image.convert()
    else:
      image = image.convert_alpha()

  except pygame.error, message:
    print "Cannot load image: %s" % (fullPath)
    raise SystemExit, message

  return image

def main():
  pygame.init()
  screen = pygame.display.set_mode((500, 500))

  background = pygame.Surface(screen.get_size())
  background.fill((250, 250, 250))

  kitten = Kitten()
  allsprites = pygame.sprite.RenderPlain((kitten))

  running = True
  while running:
    #Handle Input Events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False

    kitten.update()

    screen.blit(background, (0, 0))
    allsprites.draw(screen) 
    pygame.display.update()

  pygame.quit() 

if __name__ == '__main__':
  main()