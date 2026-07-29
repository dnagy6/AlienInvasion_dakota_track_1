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
        """Create a full 2D grid fleet of aliens with row and column spacing."""
        self.fleet.empty()

        alien_width = self.settings.alien_width
        alien_height = self.settings.alien_height
        screen_width = self.settings.screen_width
        screen_height = self.settings.screen_height

        fleet_width, fleet_height = self.calculate_fleet_size(
            alien_width, screen_width, alien_height, screen_height
        )

        x_offset, y_offset = self.calculate_offsets(
            alien_width, alien_height, screen_width, fleet_width, fleet_height
        )

        self._create_rectangle_fleet(
            alien_width, alien_height, fleet_width, fleet_height, x_offset, y_offset
        )

    def _create_rectangle_fleet(self, alien_width, alien_height, fleet_width, fleet_height, x_offset, y_offset):
        """Loop through rows and columns to spawn aliens with grid spacing."""
        for row in range(fleet_height):
            for col in range(fleet_width):
                # Skip even slots to create 1-alien gap spacing horizontally and vertically
                if col % 2 == 0 or row % 2 == 0:
                    continue

                current_x = alien_width * col + x_offset
                current_y = alien_height * row + y_offset
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_width, alien_height, screen_width, fleet_width, fleet_height):
        """Calculate start x and y coordinates to position the fleet cleanly on the right half."""
        screen_height = self.settings.screen_height
        
        fleet_horizontal_space = fleet_width * alien_width
        fleet_vertical_space = fleet_height * alien_height

        # Position fleet starting in the right half of the screen
        x_offset = int(screen_width - fleet_horizontal_space - alien_width)
        y_offset = int((screen_height - fleet_vertical_space) // 2)

        return x_offset, y_offset

    def calculate_fleet_size(self, alien_width, screen_width, alien_height, screen_height):
        """Calculate max possible rows and columns for the screen dimensions."""
        # Restrict fleet width to the right side of the screen so it doesn't spawn on top of the ship
        fleet_width = (screen_width // 2) // alien_width
        fleet_height = screen_height // alien_height

        # Keep numbers odd for clean modulo grid alignment
        if fleet_width % 2 == 0:
            fleet_width -= 1
        else:
            fleet_width -= 2

        if fleet_height % 2 == 0:
            fleet_height -= 1
        else:
            fleet_height -= 2

        return max(1, fleet_width), max(1, fleet_height)

    def _create_alien(self, current_x: int, current_y: int):
        """Helper to instantiate an alien and add it to the Pygame group."""
        new_alien = Alien(self, current_x, current_y)
        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        """Return True if ANY alien in the fleet hits a vertical screen edge."""
        for alien in self.fleet.sprites():
            if alien.check_edges():
                return True
        return False

    def update(self):
        """Update positions of all aliens in the fleet."""
        # When ANY alien touches an edge, flip vertical movement and shift the ENTIRE grid left
        if self._check_fleet_edges():
            self.settings.fleet_direction *= -1
            for alien in self.fleet.sprites():
                alien.x -= self.settings.fleet_shift_speed
                alien.rect.x = alien.x

        # Move each alien vertically
        self.fleet.update()

    def draw(self):
        """Draw all aliens in the fleet."""
        for alien in self.fleet:
            alien.draw_alien()