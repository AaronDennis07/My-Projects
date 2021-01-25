import pygame
from game_functions import Game_Functions
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
from Gamestats import game_stats
from button import Button
from score_board import ScoreBoard
def run_game():
    pygame.init()
    gf = Game_Functions()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.width,ai_settings.height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(aliens,ai_settings,screen,ship)
    #print(aliens)
    alien = Alien(screen, ai_settings)
    stats = game_stats(ai_settings)
    button = Button(screen,ai_settings,"Play")
    sb = ScoreBoard(screen,ai_settings,stats)
    while True:                             #Game loop
        gf.check_events(button,stats,aliens,bullets,screen,ship,ai_settings,sb)

        if stats.game_active:
            ship.update(ai_settings.speed)
            gf.update_bullet(bullets,aliens,ai_settings,ship,screen,stats,sb)
            gf.update_aliens(aliens,ai_settings,screen,ship,stats,bullets,sb)

        gf.update_screen(ai_settings, screen, ship, bullets,aliens,button,stats,sb)

run_game()
