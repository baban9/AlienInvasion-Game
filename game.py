"""Main Alien Invasion game loop."""

import sys

import pygame

from alien import Fleet
from bullet import Bullet
from collisions import alien_reached_bottom
from game_stats import GameStats
from hud import HUD
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Manage game assets, state, and the main loop."""

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.screen = self._create_screen()
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self.settings)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.fleet = Fleet(self)
        self.hud = HUD(self)
        self.level_flash_until = 0

    def _create_screen(self):
        if self.settings.fullscreen:
            screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = screen.get_rect().width
            self.settings.screen_height = screen.get_rect().height
            return screen
        return pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

    def run_game(self):
        self.hud.show_start_screen()
        pygame.display.flip()

        while True:
            self.clock.tick(60)
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self.fleet.update()
                self._update_aliens()

            self._update_screen()

    def start_game(self):
        self.settings = Settings()
        self.stats = GameStats(self.settings)
        self.stats.game_active = True
        self.ship = Ship(self)
        self.bullets.empty()
        self.fleet = Fleet(self)
        self.fleet.create_fleet()
        self.level_flash_until = 0

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key in (pygame.K_RIGHT, pygame.K_d):
            self.ship.moving_right = True
        elif event.key in (pygame.K_LEFT, pygame.K_a):
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE and self.stats.game_active:
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.stats.game_active and not self.stats.game_over:
            self.start_game()
        elif event.key == pygame.K_r and self.stats.game_over:
            self.start_game()
        elif event.key == pygame.K_f:
            self.settings.fullscreen = not self.settings.fullscreen
            self.screen = self._create_screen()
            self.ship = Ship(self)
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key in (pygame.K_RIGHT, pygame.K_d):
            self.ship.moving_right = False
        elif event.key in (pygame.K_LEFT, pygame.K_a):
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_aliens(self):
        if pygame.sprite.spritecollideany(self.ship, self.fleet.aliens):
            self._ship_hit()
            return

        for alien in self.fleet.aliens.sprites():
            if alien_reached_bottom(alien.rect, self.settings.screen_height):
                self._fleet_reached_bottom()
                return

        collisions = pygame.sprite.groupcollide(
            self.fleet.aliens,
            self.bullets,
            True,
            True,
        )
        if collisions:
            self.stats.score += len(collisions) * self.settings.alien_points

        if self.fleet.is_empty():
            self.bullets.empty()
            self.stats.advance_level()
            self.fleet.create_fleet()
            self.settings.fleet_direction = 1
            self.level_flash_until = pygame.time.get_ticks() + 900
            self.ship.center_ship()

    def _ship_hit(self):
        if self.bullets:
            self.bullets.empty()
        self.stats.lose_life()
        if self.stats.game_active:
            self.fleet.create_fleet()
            self.settings.fleet_direction = 1
            self.ship.center_ship()
        else:
            self.stats.game_over = True

    def _fleet_reached_bottom(self):
        self.stats.ships_left = 0
        self.stats.game_active = False
        self.stats.game_over = True
        self.stats.high_score = max(self.stats.high_score, self.stats.score)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        if self.stats.game_active:
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.fleet.draw()

        self.hud.show_score()

        now = pygame.time.get_ticks()
        if not self.stats.game_active and not self.stats.game_over:
            self.hud.show_start_screen()
        elif self.stats.game_over:
            self.hud.show_game_over()
        elif now < self.level_flash_until:
            self.hud.show_level_up()

        pygame.display.flip()


def main():
    AlienInvasion().run_game()


if __name__ == "__main__":
    main()
