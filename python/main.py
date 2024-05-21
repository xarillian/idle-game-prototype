import pygame

from villager import Villager


def initialize_villagers(count: int, screen_width: int, screen_height: int):
    """
    Initializes a list of villagers.

    Args:
        count (int): The number of villagers.
        screen_width (int): The width of the screen.
        screen_height (int): The height of the screen.
    
    Returns:
        list: A list of Villager instances.
    """
    return [Villager(screen_width, screen_height) for _ in range(count)]



def update_villagers(villagers: list, screen_width: int, screen_height: int):
    """
    Updates all villagers in the simulation.

    Args:
        villagers (list): A list of Villager instances.
        screen_width (int): The current width of the screen.
        screen_height (int): The current height of the screen.
    """
    for villager in villagers:
        villager.update_position(screen_width, screen_height)


def render_villagers(view, villagers: list[Villager]):
    """
    Renders all villagers on the screen.

    Args:
        view: The Pygame display surface.
        villagers (list): A list of Villager instances.
    """
    view.fill((0, 0, 0))
    for villager in villagers:
        pygame.draw.circle(
            view, 
            (255, 255, 255), 
            (int(villager.position[0]), int(villager.position[1])), 
            5
        )
    pygame.display.flip()


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

        update_villagers(villagers, screen_width, screen_height)
        render_villagers(screen, villagers)

        clock.tick(60)  # Maintain 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
