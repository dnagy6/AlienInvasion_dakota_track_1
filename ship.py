import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """A class to manage the player's ship."""
    
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        """Initialize the ship and set its starting position to 'midleft' rather than original position
            of 'midbottom'. This will change the orientation and feel of the gameplay for the player."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.boundaries = game.screen.get_rect()

        # self.image = pygame.image.load(self.settings.ship_file)
        # self.image = pygame.transform.scale(self.image, (
        #     self.settings.ship_width, self.settings.ship_height))

        # M1 update - loading the image with transparency and cropping away all empty tranparent
        # margins around the ship artwork
        raw_image = pygame.image.load(self.settings.ship_file).convert_alpha()

        bounding_box = raw_image.get_bounding_rect()
        trimmed_image = raw_image.subsurface(bounding_box)

        # M1 update - rotating the ship clockwise so it faces directly to the right
        scaled_image = pygame.transform.scale(
            trimmed_image, (self.settings.ship_width, self.settings.ship_height)
        )
        self.image = pygame.transform.rotate(scaled_image, -90)

        # M1 update - changed the orientation of the ship to be midleft rather than midbottom
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        self.arsenal = arsenal

    def update(self):
        """Update the ships position based on active movement flags declared in 'init'."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        temp_speed = self.settings.ship_speed

        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += temp_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= temp_speed

        self.rect.y = self.y
        self.rect.x = self.x

    def draw(self):
        """Drawing the ship at its current location."""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        return self.arsenal.fire_bullet()
