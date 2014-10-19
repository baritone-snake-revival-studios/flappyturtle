import pygame
import sys

__author__ = 'neil@everymundo.com'


class Obstacle(object):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path)

        self.pos_x = x
        self.pos_y = y - self.image.get_height()

    def update(self, velocity):
        self.pos_x += velocity

    def check_collision(self, bounds):
        bounds_left = bounds[0]
        bounds_up = bounds[1]
        bounds_right = bounds[2]
        bounds_down = bounds[3]

        if self.pos_x < bounds_right < self.pos_x + self.image.get_width():
            if self.pos_y < bounds_down < self.pos_y + self.image.get_height():
                pygame.quit()
                sys.exit()
