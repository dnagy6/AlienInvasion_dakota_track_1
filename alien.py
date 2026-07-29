"""
Program: Alien Invasion (Track 1 Side-Scroller)
Author: Dakota Nagy
Purpose: Defines the Alien sprite class for enemy fleet creation and vertical/horizontal movement.
Starter Code: Adapted from 'Python Crash Course' by Eric Matthes (3rd Edition), modified for side-scroller mechanics.
Date: July 29, 2026
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
from utilities import prepare_image

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, game: 'AlienInvasion', x: float, y: float):

        super().__init__()
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.alien_width, self.settings.alien_height)
        )

        self.rect = self.image.get_rect()
        self.rect.right = self.boundaries.right - y
        self.rect.y = y

        # smooth movement
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def check_edges(self):
        """Return True if alien hits the TOP or BOTTOM screen boundary."""
        screen_rect = self.screen.get_rect()
        return self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0

    def update(self):
        """Move the alien vertically based on current FLEET direction."""
        if self.check_edges():
            self.settings.fleet_direction *= -1
            self.x -= self.settings.fleet_shift_speed
            self.rect.x = self.x
        
        self.y += self.settings.fleet_speed * self.settings.fleet_direction
        self.rect.y = self.y
        pass

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)

        