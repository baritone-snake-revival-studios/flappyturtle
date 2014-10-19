import sys
import pygame
from flappyturtle.display.window import Window
from flappyturtle.player.turtle import Turtle
from flappyturtle.world import World


__author__ = 'neil@everymundo.com'


def run_game():
    pygame.init()
    window = Window(800, 600)
    DISPLAY_SURFACE = pygame.display.set_mode(window.dimensions)
    pygame.display.set_caption("Flappy Turtle")

    FPS = 60
    FpsClock = pygame.time.Clock()

    game_world = World(window.width, window.height)
    game_turtle = game_world.add_player(window.center())

    time_last_update = 0

    while True:
        time = FpsClock.get_time()
        # Check the keyboard & mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game_turtle.swim(up=True)
                if event.key == pygame.K_DOWN:
                    game_turtle.swim(up=False)

        game_turtle.update((time - time_last_update) / 1000)
        game_world.update((time - time_last_update) / 1000)

        DISPLAY_SURFACE.fill((55, 180, 200))
        # Background
        DISPLAY_SURFACE.blit(game_world.background, (0, 0))
        # Scrolling Sand
        DISPLAY_SURFACE.blit(game_world.sand_image, (game_world.sand_pos, window.height - game_world.sand_image.get_height()))
        # Player
        DISPLAY_SURFACE.blit(game_turtle.image, game_turtle.position())

        pygame.display.update()
        FpsClock.tick(FPS)



if __name__ == '__main__':
    run_game()