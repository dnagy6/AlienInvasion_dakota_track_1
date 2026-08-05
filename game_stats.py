"""
Program: Alien Invasion (Track 1 Side-Scroller)
Author: Dakota Nagy
Purpose: Tracks and manages real-time game stats, remaining player lives, and game-over states.
Starter Code: Adapted from 'Python Crash Course' by Eric Matthes (3rd Edition), modified for side-scroller lifecycle.
Date: July 29, 2026
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion




class GameStats():
    def __init__(self, game: 'AlienInvasion'):
        """Starting stats."""
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()

    def reset_stats(self):
        """initialize statistics that can change during the game."""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1


    def update(self, collisions):
        # update score
        self._update_score(collisions)

        # update max_score
        self._update_max_score()

        # update high score

    def _update_max_score(self):
        if self.score > self.max_score:
            self.max_score = self.score
        print(f'Max: {self.max_score}')

    def _update_score(self, collisions):
        for alien in collisions.values():
            self.score += self.settings.alien_points
        print(f'Basic: {self.score}')
        

    def update_level(self):
        self.level += 1