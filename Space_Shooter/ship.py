import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, screen):
        super(Ship,self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect =  screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
    def update(self,speed):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += speed
            #verification
            """"print(f" rect r {self.rect.right}")
            print(f" screen r {self.screen_rect.right}")
       """
        elif self.moving_left and self.rect.left > self.screen_rect.left :
            self.rect.centerx -= speed
            #verification
            """     print(f" rect l {self.rect.left}")
            print(f" screen l {self.screen_rect.left}")
    """
    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.rect.centerx = self.screen_rect.centerx