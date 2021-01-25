import pygame.font
from pygame.sprite import Group
from ship import Ship

class ScoreBoard():
    def __init__(self,screen,ai_settings,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,40)
        self.prep_score()
        self.prep_high_score()
        self.prep_ships()
    def prep_score(self):

        self.rounded_score = int(round(self.stats.score))
        score_str = "Score: {:,}".format(self.rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bgcolor)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 80
        self.score_rect.top = self.screen_rect.top


    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):

        self.rounded_high_score = int(round(self.stats.score))
        score_str = "High Score: {:,}".format(self.rounded_high_score)
        self.high_score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bgcolor)
        self.high_score_rect = self.score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx - 60
        self.high_score_rect.top = self.screen_rect.top

    def prep_ships(self):

        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
