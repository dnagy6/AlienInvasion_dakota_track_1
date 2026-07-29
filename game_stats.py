class GameStats():
    def __init__(self, ship_limit):
        """Starting stats."""
        self.ship_limit = ship_limit
        self.reset_stats()

    def reset_stats(self):
        """initialize statistics that can change during the game."""
        self.ships_left = self.ship_limit