import pygame, os, wikiapi, urllib

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

class WikipediaSprite(Sprite):
  def __init__(self, article_name):
    self.article_name = article_name
    self.image_name = self.download_wikipedia_image(article_name)
    Sprite.__init__(self, self.image_name)

  def download_wikipedia_image(self, name):
    wikiapi.WikiApi().get_article(name)
    image_url = wikiapi.WikiApi().get_article(name).image
    image_name = name + '.jpg'
    urllib.URLopener().retrieve(image_url, 'images/' + image_name)
    return image_name