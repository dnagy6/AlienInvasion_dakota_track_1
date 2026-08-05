"""
Program: Alien Invasion (Track 1 Side-Scroller)
Author: Dakota Nagy
Purpose: Defines the Alien sprite class for enemy fleet creation and vertical/horizontal movement.
Starter Code: Adapted from 'Python Crash Course' by Eric Matthes (3rd Edition), modified for side-scroller mechanics.
Date: August 9, 2026
"""

from typing import TYPE_CHECKING
import pygame
from pygame.sprite import Sprite

if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, fleet: 'AlienFleet', x: float, y: float):
        super().__init__()
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(
            self.image, (self.settings.alien_width, self.settings.alien_height)
        )
        self.rect = self.image.get_rect()

        self.x = float(x)
        self.y = float(y)
        self.rect.x = self.x
        self.rect.y = self.y

    def check_edges(self):
        """Return True if alien hits top HUD boundary or bottom screen edge."""
        screen_rect = self.screen.get_rect()
        
        if self.rect.top <= self.settings.hud_height:
            return True
        if self.rect.bottom >= screen_rect.bottom:
            return True
        return False

    def update(self):
        """Move alien vertically based on fleet direction."""
        self.y += self.settings.fleet_speed * self.settings.fleet_direction
        self.rect.y = self.y

    def draw_alien(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

        