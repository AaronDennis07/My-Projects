import sys
import pygame
from bullets import Bullet
from alien import Alien
import random
import time

class Game_Functions:

    def check_keydown_event(self, event, ship, ai_settings, bullets,screen):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self.fire_bullet(ai_settings,screen,ship,bullets)

    def check_keyup_event(self, event, ship):
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False

    def check_events(self,button,stats,aliens,bullets,screen,ship,ai_settings,sb):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_event(event,ship,ai_settings, bullets,screen)
            elif event.type == pygame.KEYUP:
                self.check_keyup_event(event,ship)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x,mouse_y = pygame.mouse.get_pos()

                self.check_play_button(button,stats,mouse_x,mouse_y,aliens,bullets,screen,ship,ai_settings,sb)

    def check_play_button(self,button,stats,mouse_x,mouse_y,aliens,bullets,screen,ship,ai_settings,sb):
        button_clicked = button.rect.collidepoint(mouse_x,mouse_y)

        if button_clicked and not stats.game_active:
            ai_settings.dynamic_setttings()
            pygame.mouse.set_visible(False)
            stats.reset()
            stats.game_active = True
            stats.score = 0
            sb.prep_score()
            sb.prep_high_score()
            sb.prep_ships()
            aliens.empty()
            bullets.empty()
            self.create_fleet(aliens, ai_settings, screen, ship)
            ship.center_ship()
            stats.score = 0



    def update_screen(self, ai_setting,screen, ship, bullets,aliens,button,stats,sb):
        bgcolor = (ai_setting.bgcolor)
        screen.fill(bgcolor)
        for bullet in bullets.sprites():
            bullet.draw_bullet()
        ship.blitme()
        for alien in aliens.sprites():
            alien.blitme()
        if not stats.game_active:
            button.draw_button()
        sb.show_score()
        pygame.display.flip()


    def update_bullet(self ,bullets,aliens,ai_settings,ship,screen,stats,sb):
        bullets.update()

        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        self.check_bullet_alien_collison(bullets,aliens,ai_settings,ship,screen,stats,sb)

    def check_bullet_alien_collison(self,bullets,aliens,ai_settings,ship,screen,stats,sb):

        collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                stats.score += ai_settings.alien_points
                sb.prep_score()
            self.check_high_score(sb,stats)

        if len(aliens) == 0:
            bullets.empty()
            ai_settings.increase_speed()
            self.create_fleet(aliens, ai_settings, screen, ship)

    def fire_bullet(self, ai_settings,screen,ship,bullets):
        if len(bullets) < ai_settings.bulletlimit:
            newBullet = Bullet(ai_settings, ship, screen)
            bullets.add(newBullet)

    def get_number_of_aliens(self,ai_settings,alien_width):

        available_space_x = ai_settings.width - 2 * alien_width
        number_of_aliens_x = int(available_space_x / (2 * alien_width))
        return number_of_aliens_x

    def get_number_of_rows(self, ai_settings, ship_height,alien_height):
        available_space_y = (ai_settings.height - (3* alien_height)- ship_height)
        number_of_rows = int(available_space_y/(2*alien_height))
        return number_of_rows

    def create_alien(self,aliens,screen,ai_settings,alien_number,row_number):
        alien = Alien(screen, ai_settings)
        alien_width = alien.rect.width
        alien_x = alien_width + 2 * alien_number * alien_width
        alien.rect.x = alien_x
        #print(alien_x)
        alien.rect.y = alien.rect.height + 2*alien.rect.height * row_number
        aliens.add(alien)

    def create_fleet(self,aliens,ai_settings,screen,ship):
        alien = Alien(screen,ai_settings)
        number_of_aliens_x = self.get_number_of_aliens(ai_settings,alien.rect.width)
        number_of_rows = self.get_number_of_rows(ai_settings,ship.rect.height,alien.rect.height)
        for row_number in range(number_of_rows):
            for alien_number in range(number_of_aliens_x):
                self.create_alien(aliens,screen,ai_settings,alien_number,row_number)

    def check_fleet_edges(self,aliens,ai_settings):

        for alien in aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction(aliens,ai_settings)
                break

    def change_fleet_direction(self, aliens, ai_settings):

        for alien in aliens.sprites():
            alien.rect.y += ai_settings.fleetdropspeed
#            alien.update()
        ai_settings.fleetdirection *= -1

    def update_aliens(self,aliens,ai_settings,screen,ship,stats,bullets,sb):
        self.check_fleet_edges(aliens,ai_settings)
        aliens.update()

        if pygame.sprite.spritecollideany(ship,aliens):
            self.ship_hit(aliens,ai_settings,screen,ship,stats,bullets,sb)
        self.check_alien_bottom(aliens,ai_settings,screen,ship,stats,bullets,sb)
    def ship_hit(self,aliens,ai_settings,screen,ship,stats,bullets,sb):

        if stats.ships_left > 0:
            stats.ships_left -= 1
            sb.prep_ships()
            print(stats.ships_left)
            aliens.empty()
            bullets.empty()
            self.create_fleet(aliens,ai_settings,screen,ship)
            ship.center_ship()
            time.sleep(0.5)

        else:
            stats.game_active = False
            pygame.mouse.set_visible(True)

    def check_alien_bottom(self, aliens,ai_settings,screen,ship,stats,bullets,sb):
        screen_rect = screen.get_rect()
        for alien in aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ship_hit(aliens,ai_settings,screen,ship,stats,bullets,sb)


    def check_high_score(self,sb,stats):
        if stats.score > stats.high_score:
            stats.high_score = stats.score
            sb.prep_high_score()