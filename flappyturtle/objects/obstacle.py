import pygame

__author__ = 'neil@everymundo.com'


class Obstacle(object):
    def __init__(self, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path)

        self.pos_x = 0
        self.pos_y = 0

    def update(self, velocity):
        self.pos_x += velocity