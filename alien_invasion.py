

import pygame

from setting import Settings
from ship import Ship
import game_functions as gf
from alien import Alien
from pygame.sprite import Group


def run_game():
    # Initializes pygame, setting and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    #Make a Ship
    ship = Ship(ai_settings, screen)

    # Make a group to store bullets in
    bullets = Group()
    aliens = Group()

    # create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()

        gf.update_bullets(bullets)
        gf.update_aliens(ai_settings, aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()