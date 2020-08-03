import pygame

from pygame.sprite import Sprite

class Bullet(Sprite):
    """A Class to manage the bullets fired form the ship"""
    def __init__(self, ai_settings, screen, ship):
        # Creates a bullet object at the ship's current position
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Stores the bullets position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Moves the bullet up the screen."""
        # Updates the decimal position of the bullet
        self.y -= self.speed_factor
        # Updates the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)





