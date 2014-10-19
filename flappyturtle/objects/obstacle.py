import pygame

__author__ = 'neil@everymundo.com'


class Obstacle(object):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path)

        self.pos_x = x
        self.pos_y = y - self.image.get_height()



    def update(self, velocity):
        self.pos_x += velocity