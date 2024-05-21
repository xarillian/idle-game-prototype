import time
import pygame

from pt.villager import Villager


INTERACTION_RADIUS = 30


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
            (int(villager.position.x), int(villager.position.y)), 
            5
        )
    pygame.display.flip()


def update_villagers(villagers: list[Villager], screen_width: int, screen_height: int):
    """
    Updates all villagers in the simulation.

    Args:
        villagers (list): A list of Villager instances.
        screen_width (int): The current width of the screen.
        screen_height (int): The current height of the screen.
    """
    for villager in villagers:
        villager.update_position(screen_width, screen_height)


def interaction_check(villagers: list[Villager]):
    """
    Checks for interactionable villagers.

    Args:
        villagers (list[Villager]): A list of Villager instances.
    
    Returns:
        tuple[Villager, Villager]: A pair of villagers if they are within an interactable radius.
    """
    for i, villager1 in enumerate(villagers):
        for villager2 in villagers[i + 1:]:
            distance = villager1.position.distance_to(villager2.position)
            if distance < INTERACTION_RADIUS:
                return villager1, villager2
    return None


def zoom_in(screen, villagers, villager1, villager2):
    """
    Zooms in on the interaction between two villagers.

    Args:
        screen: The Pygame display surface.
        villagers (list): A list of Villager instances.
        villager1: The first villager involved in the interaction.
        villager2: The second villager involved in the interaction.
    """
    # Define zoom-in rectangle
    min_x = min(villager1.position.x, villager2.position.x) - INTERACTION_RADIUS
    min_y = min(villager1.position.y, villager2.position.y) - INTERACTION_RADIUS
    max_x = max(villager1.position.x, villager2.position.x) + INTERACTION_RADIUS
    max_y = max(villager1.position.y, villager2.position.y) + INTERACTION_RADIUS

    zoom_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)
    zoomed_view = pygame.Surface((zoom_rect.width, zoom_rect.height))

    # Render the zoomed-in view
    render_villagers(zoomed_view, villagers)
    zoomed_view = pygame.transform.scale(zoomed_view, (screen.get_width(), screen.get_height()))
    screen.blit(zoomed_view, (0, 0))
    pygame.display.flip()

    # Pause for 5 seconds
    time.sleep(5)
