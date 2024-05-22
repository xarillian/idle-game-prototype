import pygame

from pt.config import INITIAL_SCREEN_HEIGHT, INITIAL_SCREEN_WIDTH
from pt.game import handle_interaction
from pt.render import (
    interaction_check,
    render_villagers,
)
from pt.setup import initialize_components
from pt.villager import DEFAULT_SPEED_FACTOR, update_villagers
from pt.ui_elements import DebugMenu, SpeedSlider


def main_loop(screen_width, screen_height):
    """
    Main game loop.

    Args:
        screen_width (int): Initial width of the game screen.
        screen_height (int): Initial height of the game screen.
    """
    # TODO okay, this works, buuuuut
    # TODO managers?
    screen, client, villagers = initialize_components()
    clock = pygame.time.Clock()
    slider = SpeedSlider(screen, screen_width, screen_height, 200, 20, 1, 10)
    debug_menu = DebugMenu(screen, screen_height)

    running = True
    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen_width, screen_height = event.w, event.h
                screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
                slider = SpeedSlider(screen, screen_width, screen_height, 200, 20, 1, 5)
                debug_menu.update_positions(screen_height)

            slider.handle_event(event)
            debug_menu.handle_event(event)

        interaction = interaction_check(villagers, current_time)
        if interaction:
            handle_interaction(screen, client, interaction)

        screen.fill((0, 0, 0))
        if debug_menu.is_speed_slider_checked():
            update_villagers(villagers, slider.current_speed, screen_width, screen_height)
        else:
            update_villagers(villagers, DEFAULT_SPEED_FACTOR, screen_width, screen_height)

        render_villagers(screen, villagers)
        if debug_menu.is_speed_slider_checked():
            slider.render()
        debug_menu.render()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main_loop(INITIAL_SCREEN_WIDTH, INITIAL_SCREEN_HEIGHT)
