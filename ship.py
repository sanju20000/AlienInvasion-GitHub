import pygame

class Ship():

    def __init__(self, screen):
        """Initializes the ship and set its starting position"""
        self.screen = screen

        # Load the ship images and get its rect
        self.image = pygame.image.load('Images/Ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit (self.image, self.rect)