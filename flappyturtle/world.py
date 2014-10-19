import os
import pygame
from flappyturtle.objects.obstacle import Obstacle
from flappyturtle.player.turtle import Turtle

__author__ = 'neil@everymundo.com'


class World():
    def __init__(self, width, height):
        super().__init__()
        self.turtle = None
        self.obstacles = []
        self.width = width
        self.height = height
        self.background = pygame.image.load(os.path.join('sprites', 'background.png'))
        scale_x = self.width / self.background.get_width()
        scale_y = self.height / self.background.get_height()
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.background_pos = 0
        self.sand_image = pygame.image.load(os.path.join('sprites', 'background_sand.png'))
        self.sand_image = pygame.transform.scale(self.sand_image,
                                                 (self.width, int(self.sand_image.get_height() * scale_x)))
        self.sand_pos = 0
        self.velocity = 1000

    def add_player(self, position):
        self.turtle = Turtle(position)
        return self.turtle

    def add_obstacle(self, obstacle_type):
        if obstacle_type == 'coral':
            self.obstacles.append(Obstacle('sprites/coral.png'))

    def update(self, time):
        turtle_bounds = self.turtle.bounds()
        if turtle_bounds[1] <= 0:
            self.turtle.too_high(0)
        if turtle_bounds[3] >= self.height:
            self.turtle.too_low(self.height)

        self.sand_pos -= self.velocity * time
        if self.sand_pos <= -self.width:
             self.sand_pos += self.width

        self.background_pos -= self.velocity * time
        if self.background_pos <= -self.width:
             self.background_pos += self.width

        for obstacle in self.obstacles:
            obstacle.pos_x -= self.velocity * time
