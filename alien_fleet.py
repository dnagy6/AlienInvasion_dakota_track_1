"""
Program: Alien Invasion (Track 1 Side-Scroller)
Author: Dakota Nagy
Purpose: 
Starter Code: Adapted from 'Python Crash Course' by Eric Matthes (3rd Edition), modified for side-scroller mechanics.
Date: July 29, 2026
"""

import pygame
from alien import Alien

class AlienFleet:
    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()

    def create_fleet(self):
        """Create a vertical column of aliens on the right side of the screen."""
        alien_height = self.settings.alien_height
        screen_height = self.settings.screen_height

        fleet_height = self.calculate_fleet_size(alien_height, screen_height)

        # Calculate vertical offset to center the column
        fleet_vertical_space = fleet_height * alien_height
        y_offset = int((screen_height - fleet_vertical_space) // 2)

        # Place the column near the right edge of the screen
        start_x = self.settings.screen_width - (2 * self.settings.alien_width)

        for row in range(fleet_height):
            current_y = (alien_height * row) + y_offset
            self._create_alien(start_x, current_y)

    def calculate_fleet_size(self, alien_height, screen_height):
        """Calculate how many aliens fit vertically in a column."""
        fleet_height = screen_height // alien_height
        
        # Keep an odd count for clean centering spacing
        if fleet_height % 2 == 0:
            fleet_height -= 1
        else:
            fleet_height -= 2
            
        return max(1, fleet_height)

    def _create_alien(self, current_x: int, current_y: int):
        """Helper to instantiate an alien and add it to the Pygame group."""
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        """Return True if ANY alien in the fleet has hit a vertical edge."""
        for alien in self.fleet.sprites():
            if alien.check_edges():
                return True
        return False

    def update(self):
        """Update positions of all aliens in the fleet."""
        # If any alien hits an edge, flip direction and shift the WHOLE fleet left
        if self._check_fleet_edges():
            self.settings.fleet_direction *= -1
            for alien in self.fleet.sprites():
                alien.x -= self.settings.fleet_shift_speed
                alien.rect.x = alien.x

        # Move each alien vertically
        self.fleet.update()

    def draw(self):
        """Draw all aliens in the fleet to the screen."""
        for alien in self.fleet:
            alien.draw_alien()