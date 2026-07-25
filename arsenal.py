"""
Program: Alien Invasion (Track 1 Side-Scroller)
Author: Dakota Nagy
Purpose: Manages active bullet groups, firing constraints, and off-screen sprite cleanup.
Starter Code: Custom architecture created to encapsulate projectile management (DRY design).
Date: July 25, 2026
"""


import pygame
from typing import TYPE_CHECKING
from bullet import Bullet

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Arsenal:
    """Class to manage bullet creation, updates, and screen cleanup."""

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the arsenal group."""
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        """Update bullet positions and cull off-screen bullets."""
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self) -> None:
        """Remove bullets that have traveled past the right edge of the screen."""
        for bullet in self.arsenal.copy():
            if bullet.rect.left >= self.settings.screen_width:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """Draw all active bullets to the screen."""
        for bullet in self.arsenal.sprites():
            bullet.draw_bullet()

    def fire_bullet(self) -> bool:
        """Fire a new bullet if limit has not been reached."""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False