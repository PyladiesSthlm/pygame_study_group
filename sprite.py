import pygame, os

class Sprite(pygame.sprite.Sprite):
  def __init__(self, imageName):
    pygame.sprite.Sprite.__init__(self) #call Sprite intializer
    self.image = self.load_image(imageName)
    self.rect = self.image.get_rect()
    self.rect.center = (250, 250)

  def load_image(self, imageName):
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

  def update(self):
    self.rect.topleft = pygame.mouse.get_pos()