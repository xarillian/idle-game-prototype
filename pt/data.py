
import json


def create_new_villager_data(villagers):
    """
    Creates a dictionary to store villager data.

    Args:
        villagers (list): A list of Villager instances.

    Returns:
        dict: A dictionary with villager data.
    """
    villager_data = {}
    for villager in villagers:
        villager_data[villager.id] = {
            'name': villager.name,
            'core_personality': villager.personality_traits,
            'memory': {
                'other_villagers': {},
                'history': [
                    'You came from far away, at the behest of your king, to settle an uninhabited land.'
                ]
            },
            'flags': {
                'is_new': True  # indicate the villager is new and doesn't know anyone yet
            }
        }
    return villager_data


def load_villager_data(filename='pt/villager_info.json'):
    """
    Loads villager data from a JSON file.

    Args:
        filename (str): The path to the JSON file.

    Returns:
        dict: The loaded villager data.
    """
    with open(filename, 'r', encoding='utf-8') as villager_info_file:
        return json.load(villager_info_file)


def save_villager_data(villager_data, filename='pt/villager_info.json'):
    """
    Saves villager data to a JSON file.

    Args:
        villager_data (dict): The villager data to save.
        filename (str): The path to the JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as villager_info_file:
        json.dump(villager_data, villager_info_file, indent=4)


def update_villager_data(villager_id, updated_data, filename='pt/villager_info.json'):
    """
    Updates the data of a single villager in the JSON file.

    Args:
        villager_id (str): The ID of the villager to update.
        updated_data (dict): The updated data for the villager.
        filename (str): The path to the JSON file.
    """
    villager_data = load_villager_data(filename)
    if villager_id in villager_data:
        villager_data[villager_id].update(updated_data)
        save_villager_data(villager_data, filename)
    else:
        raise ValueError(f"Villager with ID {villager_id} does not exist.")
