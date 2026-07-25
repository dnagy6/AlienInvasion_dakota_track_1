import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Ship:
    """A class to manage the player's ship."""
    
    def __init__(self, game: 'AlienInvasion') :
        """Initialize the ship and set its starting position to 'midleft' rather than original position of 'midbottom'.
            this will change the orientation and feel of the gameplay for the player."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (
            self.settings.ship_width, self.settings.ship_height))
        # M1 update - loading the image with transparency and cropping away all empty tranparent
        # margins around the ship artwork
        raw_image = pygame.image.load(self.settings.ship_file).convert_alpha()

        bounding_box = raw_image.get_bounding_rect()
        trimmed_image = raw_image.subsurface(bounding_box)

        # M1 update - rotating the ship clockwise so it faces directly to the right
        scaled_image = pygame.transform.scale(
            trimmed_image, (self.settings.ship_width, self.settings.ship_height)
        )
        self.image = pygame.transform.rotate(self.image, -90)

        # M1 update - changed the orientation of the ship to be midleft rather than midbottom
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

    def draw(self):
        """Drawing the ship at its current location."""
        self.screen.blit(self.image, self.rect)
