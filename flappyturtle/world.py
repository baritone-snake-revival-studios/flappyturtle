from flappyturtle.objects.obstacle import Obstacle
from flappyturtle.player.turtle import Turtle

__author__ = 'neil@everymundo.com'


class World():
    def __init__(self):
        super().__init__()
        self.turtle = None
        self.obstacles = []

    def add_player(self, position):
        self.turtle = Turtle(position)
        return self.turtle

    def add_obstacle(self, obstacle_type):
        if obstacle_type == 'coral':
            self.obstacles.append(Obstacle('sprites/coral.png'))
