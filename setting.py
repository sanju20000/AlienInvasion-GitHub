class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1300
        self.screen_height = 700
        self.bg_color = (240, 210, 130)

        # Ship settings
        self.ship_speed_factor = 1.5

        # bullets settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 10
        self .bullet_color = (255, 0, 0)
        self.bullets_allowed = 4

        # Alien settings
        self.alien_speed_factor = 1