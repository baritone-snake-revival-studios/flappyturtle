"""
Pixel perfect collision algorithm
From http://www.pygame.org/wiki/FastPixelPerfect?parent=CookBook
"""
import pygame


def pixel_perfect_check_collision(obj1, obj2):
    image_mask = pygame.mask.from_surface(obj1.image)
    otherimage_mask = pygame.mask.from_surface(obj2.image)

    offset_x = obj1.rect.left - obj2.rect.left
    offset_y = obj1.rect.top - obj2.rect.top

    if image_mask.overlap(otherimage_mask, (offset_x, offset_y)) is not None:
        return True
    else:
        return False