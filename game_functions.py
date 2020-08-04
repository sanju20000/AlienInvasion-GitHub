import sys

import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings, screen, ship, bullets):
    """Responds to key press and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    # responses the keydown events
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet"""
    # create a new bullet and add it to bullets Group
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keyup_events(event, ship):
    # responses the key realeases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Update images on the screen and flip to the new screen"""
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets behind ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    aliens.draw(screen)

    # make the most recently drawn screen visible
    pygame.display.flip()

def update_bullets(bullets):
    """Updates position of the bullet and get rid of old bullets"""
    # Update bullet positions
    bullets.update()

    # Get rid of the bullets that have disappeared
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def create_fleet(ai_settings, screen, aliens):
    """Creates a full fleet of aliens"""
    # Creates an alien and find the number of aliens in a row
    # Spacing between each alien is equal to one alien width
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / alien_width)

    # Creates the first row of the aliens
    for alien_number in range(number_alien_x):
        # creates the alien and place it in a row
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        aliens.add(alien)


