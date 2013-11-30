import pygame, wikiapi, urllib

from sprite import *

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