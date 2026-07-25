"""
Program: Alien Invasion (Track 1 Side-Scroller)
Author: Dakota Nagy
Purpose: Manages individual bullet projectile behavior moving horizontally across the screen.
Starter Code: Adapted from 'Python Crash Course' by Eric Matthes (3rd Edition), altered for rightward trajectory.
Date: July 25, 2026
"""


import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
from utilities import prepare_image

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, game: 'AlienInvasion') -> None:
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load, crop, scale, and rotate using utilities.py 
        self.image = prepare_image(
            self.settings.bullet_file,
            self.settings.bullet_width,
            self.settings.bullet_height,
            angle = -90,
        )

        self.rect = self.image.get_rect()
        self.rect.midleft = game.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self) -> None:
        """Move the bullet rightward across the screen."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self) -> None:
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)