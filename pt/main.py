import pygame

from pt.render import interaction_check, render_villagers, update_villagers, zoom_in
from pt.villager import initialize_villagers


def main():
    screen_width = 800
    screen_height = 600
    villager_count = 4

    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("idle game prototype")

    clock = pygame.time.Clock()

    villagers = initialize_villagers(villager_count, screen_width, screen_height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                screen_width, screen_height = event.w, event.h

        interaction = interaction_check(villagers)
        if interaction:
            villager1, villager2 = interaction
            zoom_in(screen, villagers, villager1, villager2)

        update_villagers(villagers, screen_width, screen_height)
        render_villagers(screen, villagers)

        clock.tick(60)  # Maintain 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
