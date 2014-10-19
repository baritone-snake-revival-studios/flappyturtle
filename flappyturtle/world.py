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

    def add_player(self, position):
        self.turtle = Turtle(position)
        return self.turtle

    def add_obstacle(self, obstacle_type):
        if obstacle_type == 'coral':
            self.obstacles.append(Obstacle('sprites/coral.png'))
    def update(self, time):
        turtle_bounds = self.turtle.bounds()
        if turtle_bounds[1] <= 0:
            self.turtle.toohigh(0)
        if turtle_bounds[3] >= self.height:
            self.turtle.toolow(self.height)
