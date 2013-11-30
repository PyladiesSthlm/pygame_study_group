import pygame, os

class Sprite(pygame.sprite.Sprite):
  def __init__(self, image_name):
    pygame.sprite.Sprite.__init__(self) #call Sprite intializer
    self.image = self.load_image(image_name)
    self.rect = self.image.get_rect()
    self.rect.center = (250, 250)
    self.being_dragged = False

  def load_image(self, image_name):
    fullPath = os.path.join("images", image_name)

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
    if self.being_dragged:
      self.rect.center = pygame.mouse.get_pos()