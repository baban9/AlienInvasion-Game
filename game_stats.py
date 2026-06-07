"""Track score, lives, and high-level game state."""


class GameStats:
    """Track scoring and lifecycle flags for Alien Invasion."""

    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.high_score = 0
        self.game_active = False
        self.game_over = False

    def reset_stats(self):
        """Reset run statistics while keeping high score."""
        self.score = 0
        self.level = 1
        self.ships_left = self.settings.ship_limit
        self.game_over = False

    def record_hit(self):
        self.score += self.settings.alien_points

    def lose_life(self):
        if self.ships_left > 0:
            self.ships_left -= 1
        if self.ships_left <= 0:
            self.game_active = False
            self.game_over = True
            self.high_score = max(self.high_score, self.score)

    def advance_level(self):
        self.level += 1
        self.settings.increase_speed()
