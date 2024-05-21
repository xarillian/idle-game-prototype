import pygame

from pt.chat import villager_chat
from pt.render import (
    clear_interaction,
    display_interaction,
    interaction_check,
    render_villagers,
    update_villagers,
)
from pt.setup import initialize_llm
from pt.villager import initialize_villagers


def main():
    screen_width = 800
    screen_height = 600
    villager_count = 4

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("idle game prototype")

    clock = pygame.time.Clock()

    client = initialize_llm()
    villagers = initialize_villagers(villager_count, screen_width, screen_height)

    running = True
    while running:
        current_time = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen_width, screen_height = event.w, event.h

        interaction = interaction_check(villagers, current_time)
        if interaction:
            villager_1, villager_2 = interaction  # TODO I hate this pattern
            original_view = screen.copy()
            display_interaction(screen)
            villager_chat(client, screen, villager_1, villager_2)
            clear_interaction(screen, original_view)

        update_villagers(villagers, screen_width, screen_height)
        render_villagers(screen, villagers)

        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
