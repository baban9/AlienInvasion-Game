"""Draw ship using vector graphics (no external assets required)."""

import pygame


def create_ship_surface(width: int, height: int) -> pygame.Surface:
    """Build a simple rocket sprite."""
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    body = pygame.Rect(width * 0.2, height * 0.2, width * 0.6, height * 0.55)
    pygame.draw.rect(surface, (70, 160, 255), body, border_radius=6)
    pygame.draw.polygon(
        surface,
        (120, 200, 255),
        [(width * 0.5, 0), (width * 0.78, height * 0.32), (width * 0.22, height * 0.32)],
    )
    pygame.draw.polygon(
        surface,
        (255, 120, 80),
        [(width * 0.5, height), (width * 0.68, height * 0.72), (width * 0.32, height * 0.72)],
    )
    return surface


class Ship:
    """Manage player ship position and rendering."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = create_ship_surface(self.settings.ship_width, self.settings.ship_height)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Reset ship to the bottom center after losing a life."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
