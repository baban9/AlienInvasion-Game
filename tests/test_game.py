"""Tests for Alien Invasion game logic."""

import pygame

from collisions import alien_hit_by_bullet, alien_hit_ship, alien_reached_bottom
from game_stats import GameStats
from settings import Settings


def test_alien_hit_by_bullet():
    alien = pygame.Rect(100, 100, 40, 30)
    bullet = pygame.Rect(110, 110, 4, 12)
    assert alien_hit_by_bullet(alien, bullet) is True


def test_alien_reached_bottom():
    alien = pygame.Rect(50, 780, 40, 30)
    assert alien_reached_bottom(alien, 800) is True
    assert alien_reached_bottom(pygame.Rect(50, 700, 40, 30), 800) is False


def test_alien_hit_ship():
    ship = pygame.Rect(200, 740, 60, 48)
    alien = pygame.Rect(210, 730, 40, 30)
    assert alien_hit_ship(alien, ship) is True


def test_level_progression_increases_difficulty():
    settings = Settings()
    initial_speed = settings.alien_speed
    stats = GameStats(settings)
    stats.advance_level()
    assert stats.level == 2
    assert settings.alien_speed > initial_speed


def test_stats_replacement_matches_start_game_pattern():
    """start_game() creates a new GameStats object; readers must use ai_game.stats."""
    settings = Settings()
    stats_before = GameStats(settings)
    stats_after = GameStats(settings)
    stats_after.advance_level()
    assert stats_before.level == 1
    assert stats_after.level == 2


def test_lose_life_triggers_game_over():
    settings = Settings()
    settings.ship_limit = 1
    stats = GameStats(settings)
    stats.lose_life()
    assert stats.game_over is True
    assert stats.game_active is False
