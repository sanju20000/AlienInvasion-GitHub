import sys

import pygame

from setting import Settings

def run_game():
    # Initializes pygame, setting and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    # Set the backgound color
    bg_color = (240, 210, 130)
    pygame.display.set_caption("Alien Invasion")

    # start the main loop for the game
    while True:

        # watch for keyboards and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_color)

        # make the most recently drawn screen visible
        pygame.display.flip()

run_game()