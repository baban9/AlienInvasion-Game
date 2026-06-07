"""Alien invaders and fleet layout."""

import pygame
from pygame.sprite import Sprite


def create_alien_surface(width: int, height: int, color: tuple[int, int, int]) -> pygame.Surface:
    """Build a simple alien sprite."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    body = pygame.Rect(4, 8, width - 8, height - 12)
    pygame.draw.ellipse(surface, color, body)
    pygame.draw.rect(surface, color, pygame.Rect(width * 0.15, 4, width * 0.7, height * 0.35), border_radius=8)
    eye_color = (20, 30, 40)
    pygame.draw.circle(surface, eye_color, (int(width * 0.35), int(height * 0.42)), 4)
    pygame.draw.circle(surface, eye_color, (int(width * 0.65), int(height * 0.42)), 4)
    return surface


class Alien(Sprite):
    """A single alien in the invasion fleet."""

    def __init__(self, ai_game, x_pos, y_pos):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = create_alien_surface(
            self.settings.alien_width,
            self.settings.alien_height,
            self.settings.alien_color,
        )
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Fleet:
    """Create and manage a grid of aliens."""

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.aliens = pygame.sprite.Group()

    def create_fleet(self):
        self.aliens.empty()
        settings = self.ai_game.settings
        alien = Alien(self.ai_game, 0, 0)
        alien_width, alien_height = alien.rect.size
        available_width = settings.screen_width - (2 * alien_width)
        number_aliens_x = max(1, available_width // (2 * alien_width))
        number_rows = 4

        for row in range(number_rows):
            for col in range(number_aliens_x):
                x_pos = alien_width + (2 * alien_width * col)
                y_pos = alien_height + (2 * alien_height * row)
                self.aliens.add(Alien(self.ai_game, x_pos, y_pos))

    def check_edges(self):
        edge_hit = False
        for alien in self.aliens.sprites():
            if alien.rect.right >= self.ai_game.settings.screen_width or alien.rect.left <= 0:
                edge_hit = True
                break
        if edge_hit:
            self.change_direction()

    def change_direction(self):
        settings = self.ai_game.settings
        settings.fleet_direction *= -1
        for alien in self.aliens.sprites():
            alien.rect.y += settings.fleet_drop_speed

    def update(self):
        self.check_edges()
        self.aliens.update()

    def draw(self):
        for alien in self.aliens.sprites():
            alien.draw()

    def is_empty(self) -> bool:
        return len(self.aliens) == 0
