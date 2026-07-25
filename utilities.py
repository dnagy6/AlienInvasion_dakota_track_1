"""
Program: Alien Invasion (Track 1 Side-Scroller)
Author: Dakota Nagy
Purpose: Helper functions for cross-platform asset loading, image scaling, cropping, and rotation.
Starter Code: Custom helper module created for image transformation pipeline reuse.
Date: July 25, 2026
"""


from pathlib import Path
import pygame


def prepare_image(
    file_path: Path | str, width: int, height: int, angle: int = -90
) -> pygame.Surface:
    """Load an image, crop transparent padding, scale to size, and rotate.

    Default rotation angle is -90 degrees (clockwise facing right).
    """
    raw_image = pygame.image.load(str(file_path)).convert_alpha()
    bounding_box = raw_image.get_bounding_rect()
    trimmed_image = raw_image.subsurface(bounding_box)
    scaled_image = pygame.transform.scale(trimmed_image, (width, height))
    return pygame.transform.rotate(scaled_image, angle)