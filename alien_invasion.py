import sys

import pygame

def run_game():
    # Initializes game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200,600))

    pygame.display.set_caption("Alien Invasion")

    # start the main loop for the game
    while True:

        # watch for keyboards and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # make the most recently drawn screen visible
        pygame.display.flip()

run_game()