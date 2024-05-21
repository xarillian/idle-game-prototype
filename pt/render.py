import pygame

from pt.villager import Villager


INTERACTION_RADIUS = 30
INTERACTION_TIMEOUT = 20000  # milliseconds (10 seconds)


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
            3
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


def interaction_check(villagers: list[Villager], current_time: float):
    """
    Checks for interactionable villagers.

    Args:
        villagers (list[Villager]): A list of Villager instances.
    
    Returns:
        tuple[Villager, Villager]: A pair of villagers if they are within an interactable radius.
    """
    for i, villager1 in enumerate(villagers):
        for villager2 in villagers[i + 1:]:
            if current_time - villager1.last_interaction > INTERACTION_TIMEOUT and \
                    current_time - villager2.last_interaction > INTERACTION_TIMEOUT:
                distance = villager1.position.distance_to(villager2.position)
                if distance < INTERACTION_RADIUS:  # TODO shouldn't set this here
                    villager1.last_interaction = current_time
                    villager2.last_interaction = current_time
                    return villager1, villager2
    return None


def display_interaction(screen):
    """
    Displays the interaction between two villagers.

    Args:
        screen: The Pygame display surface.
    """
    screen.fill((0, 0, 0))

    screen_width, screen_height = screen.get_size()
    villager1_pos = (screen_width // 4, screen_height // 2.25)
    villager2_pos = (3 * screen_width // 4, screen_height // 2.25)

    pygame.draw.circle(screen, (255, 255, 255), villager1_pos, 30)
    pygame.draw.circle(screen, (255, 255, 255), villager2_pos, 30)

    pygame.display.flip()


def clear_interaction(screen, default_view):
    """
    Clears the interaction view and restores the original screen.

    Args:
        screen: The Pygame display surface.
        default_view: The original view before the interaction.
    """
    screen.blit(default_view, (0, 0))
    pygame.display.flip()


def render_chat(screen, text: str):
    """
    Renders chat text on the screen and erases it after a delay.

    Args:
        screen: The Pygame display surface.
        text (str): The text to be rendered.
    """
    font = pygame.font.Font(None, 36)
    screen_width = screen.get_width()
    max_width = screen_width - 40  # Add some padding

    words = text.split(' ')
    lines = []
    current_line = ''

    for word in words:
        test_line = f'{current_line} {word}'.strip()
        test_surface = font.render(test_line, True, (255, 255, 255))
        if test_surface.get_width() <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    lines.append(current_line)

    y_offset = screen.get_height() // 1.5

    for line in lines:
        text_surface = font.render(line, True, (255, 255, 255))
        text_position = (
            screen_width // 2 - text_surface.get_width() // 2,
            y_offset
        )
        screen.blit(text_surface, text_position)
        y_offset += text_surface.get_height() + 5  # Add some space between lines

    pygame.display.flip()

    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < 5000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    screen.fill(
        (0, 0, 0),
        (20, screen.get_height() // 1.5 - 20, screen_width - 40, screen.get_height() - (screen.get_height() // 1.5 - 20))
    )
    pygame.display.flip()
