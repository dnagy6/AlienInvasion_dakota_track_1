"""
Program: Alien Invasion (Track 1 Side-Scroller)
Author: Dakota Nagy
Purpose: Defines the player Ship sprite, handling 4-way spatial movement and bounds checking.
Starter Code: Adapted from 'Python Crash Course' by Eric Matthes (3rd Edition), modified for midleft orientation.
Date: July 25, 2026
"""


import pygame
from typing import TYPE_CHECKING
from utilities import prepare_image


if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """A class to manage the player's ship."""
    
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        """Initialize the ship and set its starting position to 'midleft' rather than original position
            of 'midbottom'. This will change the orientation and feel of the gameplay for the player."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.boundaries = game.screen.get_rect()

        # Load, crop, scale, and rotate using utilities.py 
        self.image = prepare_image(
            self.settings.ship_file,
            self.settings.ship_width,
            self.settings.ship_height,
            angle = -90,
        )

        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        # ships movement flags
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.arsenal = arsenal

    def update(self):
        """Update the ships position based on active '# ships movement flags' declared in 'init'."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """Update ship position based on movement flags and screen boundaries."""
        temp_speed = self.settings.ship_speed

        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.y = self.y
        self.rect.x = self.x

    def draw(self):
        """Drawing the ship at its current location."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        """Delegate bullet creation to the active arsenal system."""
        return self.arsenal.fire_bullet()
