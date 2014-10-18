import sys
import pygame
from flappyturtle.display.window import Window
from flappyturtle.player.turtle import Turtle


__author__ = 'neil@everymundo.com'


def run_game():
    pygame.init()
    window = Window(800, 600)
    DISPLAY_SURFACE = pygame.display.set_mode(window.dimensions)
    pygame.display.set_caption("Flappy Turtle")

    FPS = 60
    FpsClock = pygame.time.Clock()

    game_turtle = Turtle()

    while True:
    # Check the keyboard & mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        DISPLAY_SURFACE.fill((55, 180, 200))
        DISPLAY_SURFACE.blit(game_turtle.image, [game_turtle.pos_x, game_turtle.pos_y])

        pygame.display.update()
        FpsClock.tick(FPS)




if __name__ == '__main__':
    run_game()