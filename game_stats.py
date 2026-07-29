"""
Program: Alien Invasion (Track 1 Side-Scroller)
Author: Dakota Nagy
Purpose: Tracks and manages real-time game stats, remaining player lives, and game-over states.
Starter Code: Adapted from 'Python Crash Course' by Eric Matthes (3rd Edition), modified for side-scroller lifecycle.
Date: July 29, 2026
"""

class GameStats():
    def __init__(self, ship_limit):
        """Starting stats."""
        self.ship_limit = ship_limit
        self.reset_stats()

    def reset_stats(self):
        """initialize statistics that can change during the game."""
        self.ships_left = self.ship_limit