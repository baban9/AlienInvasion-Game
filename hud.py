"""Heads-up display for score, lives, and level."""

import pygame


class HUD:
    """Render scoreboard and overlay screens."""

    def __init__(self, ai_game):
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        self.font = pygame.font.SysFont(None, 36)
        self.title_font = pygame.font.SysFont(None, 72)
        self.subtitle_font = pygame.font.SysFont(None, 32)

    def show_score(self):
        score = self.font.render(f"Score: {self.stats.score}", True, self.settings.text_color)
        level = self.font.render(f"Level: {self.stats.level}", True, self.settings.text_color)
        lives = self.font.render(f"Lives: {self.stats.ships_left}", True, self.settings.text_color)
        high = self.font.render(f"Best: {self.stats.high_score}", True, self.settings.muted_text_color)
        self.screen.blit(score, (20, 20))
        self.screen.blit(level, (20, 56))
        self.screen.blit(lives, (20, 92))
        self.screen.blit(high, (20, 128))

    def show_center_message(self, title: str, subtitle: str):
        overlay = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 120))
        self.screen.blit(overlay, (0, 0))

        title_image = self.title_font.render(title, True, self.settings.text_color)
        subtitle_image = self.subtitle_font.render(subtitle, True, self.settings.muted_text_color)
        title_rect = title_image.get_rect(center=self.screen.get_rect().center)
        subtitle_rect = subtitle_image.get_rect(
            center=(self.screen.get_rect().centerx, title_rect.bottom + 28)
        )
        self.screen.blit(title_image, title_rect)
        self.screen.blit(subtitle_image, subtitle_rect)

    def show_start_screen(self):
        self.show_center_message("Alien Invasion", "Press P to play  |  F fullscreen  |  Q quit")

    def show_game_over(self):
        self.show_center_message(
            "Game Over",
            f"Final score: {self.stats.score}  |  R restart  |  Q quit",
        )

    def show_level_up(self):
        message = self.subtitle_font.render(
            f"Level {self.stats.level}", True, self.settings.text_color
        )
        rect = message.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(message, rect)
