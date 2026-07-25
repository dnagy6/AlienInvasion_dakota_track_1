import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, game: 'AlienInvasion') -> None:
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
              
        raw_image = pygame.image.load(self.settings.bullet_file).convert_alpha()
        
        bounding_box = raw_image.get_bounding_rect()
        trimmed_image = raw_image.subsurface(bounding_box)
        
        # M1 update - rotating the bullets clockwise so it faces directly to the right
        scaled_image = pygame.transform.scale(
            trimmed_image, (self.settings.bullet_width, self.settings.bullet_height)
                )
        self.image = pygame.transform.rotate(scaled_image, -90)

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