import pygame

from pt.config import INITIAL_SCREEN_HEIGHT, INITIAL_SCREEN_WIDTH
from pt.game import handle_interaction
from pt.render import (
    interaction_check,
    render_villagers,
    update_villagers,
)
from pt.setup import initialize_components


def main_loop(screen_width, screen_height):
    """
    Main game loop.

    Args:
        screen_width (int): Initial width of the game screen.
        screen_height (int): Initial height of the game screen.
    """
    screen, client, villagers = initialize_components()
    clock = pygame.time.Clock()

    running = True
    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen_width, screen_height = event.w, event.h
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

        interaction = interaction_check(villagers, current_time)
        if interaction:
            handle_interaction(screen, client, villagers, interaction)

        update_villagers(villagers, screen_width, screen_height)
        render_villagers(screen, villagers)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main_loop(INITIAL_SCREEN_WIDTH, INITIAL_SCREEN_HEIGHT)
