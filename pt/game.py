from pt.chat import villager_chat
from pt.render import clear_interaction, display_interaction


def handle_interaction(screen, client, interaction, current_time, interaction_cooldowns):
    """ Handle interaction between villagers. """
    villager_1, villager_2 = interaction  # TODO ~~I hate this pattern~~ maybe not hate but something is fishy here
    original_view = screen.copy()
    display_interaction(screen)
    villager_chat(screen, client, villager_1, villager_2)
    pair_key = (villager_1.id, villager_2.id)
    interaction_cooldowns[pair_key] = current_time
    clear_interaction(screen, original_view)

    return current_time
