import pygame
from  pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, screen, ai_settings):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/b.png')
        self.rect =  self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)


    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):

        self.rect.x += (self.ai_settings.alienspeed * self.ai_settings.fleetdirection)
        