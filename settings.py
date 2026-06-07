"""Central configuration for Alien Invasion."""


class Settings:
    """Store all tunable game settings."""

    def __init__(self):
        # Display
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (15, 20, 35)
        self.fullscreen = False

        # Ship
        self.ship_speed = 6.0
        self.ship_width = 60
        self.ship_height = 48
        self.ship_limit = 3

        # Bullets
        self.bullet_speed = 10.0
        self.bullet_width = 4
        self.bullet_height = 18
        self.bullet_color = (255, 220, 80)
        self.bullets_allowed = 5

        # Aliens
        self.alien_width = 48
        self.alien_height = 36
        self.alien_color = (60, 220, 120)
        self.alien_points = 50
        self.fleet_drop_speed = 8
        self.fleet_direction = 1  # 1 = right, -1 = left

        # Difficulty scaling
        self.speedup_scale = 1.12
        self.score_scale = 1.05
        self.alien_speed = 1.5

        # UI
        self.text_color = (230, 230, 240)
        self.muted_text_color = (160, 170, 190)

    def increase_speed(self):
        """Raise difficulty after each level."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        self.fleet_drop_speed += 1
