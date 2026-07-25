import pygame

def prepare_image(
    file_path: str, width: int, height: int, angle: int = -90
) -> pygame.Surface:
    """Load an image, crop transparent padding, scale to size, and rotate.

    Default rotation angle is -90 degrees (clockwise facing right).
    """
    raw_image = pygame.image.load(file_path).convert_alpha()
    bounding_box = raw_image.get_bounding_rect()
    trimmed_image = raw_image.subsurface(bounding_box)
    scaled_image = pygame.transform.scale(trimmed_image, (width, height))
    return pygame.transform.rotate(scaled_image, angle)