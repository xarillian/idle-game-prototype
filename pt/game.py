from pt.chat import villager_chat
from pt.render import clear_interaction, display_interaction


def handle_interaction(screen, client, villagers, interaction):
    """
    Handle interaction between villagers.

    Args:
        client: The LLM client.
        screen: The Pygame screen surface.
        villagers (list): List of villager instances.
        interaction (tuple): Tuple containing the interacting villagers.
    """
    villager_1, villager_2 = interaction  # TODO I hate this pattern
    original_view = screen.copy()
    display_interaction(screen)
    villager_chat(screen, client, villager_1, villager_2)
    clear_interaction(screen, original_view)
