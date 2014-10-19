import os
import pygame


class Turtle(object):
    swim_speed = 175

    def __init__(self):
        super().__init__()
        self.image_path = 'sprites/turtle.png'
        self.image = pygame.image.load(os.path.join('sprites', 'turtle.png'))

        self.pos_x = 0
        self.pos_y = 0

        self.vel_x = 0
        self.vel_y = 10

    def position(self):
        return [self.pos_x, self.pos_y]

    def update(self, time):
        self.pos_y += self.vel_y * time

    def swim(self, up):
        if up:
            self.vel_y = -Turtle.swim_speed
        else:
            self.vel_y = Turtle.swim_speed