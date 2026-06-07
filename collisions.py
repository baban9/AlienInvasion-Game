"""Collision helpers (testable without pygame display)."""


def alien_hit_by_bullet(alien_rect, bullet_rect) -> bool:
    return alien_rect.colliderect(bullet_rect)


def alien_reached_bottom(alien_rect, screen_height: int) -> bool:
    return alien_rect.bottom >= screen_height


def alien_hit_ship(alien_rect, ship_rect) -> bool:
    return alien_rect.colliderect(ship_rect)
