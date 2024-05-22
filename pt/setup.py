import os
import random
import pygame
import openai

from dotenv import load_dotenv

from pt.config import INITIAL_SCREEN_WIDTH, INITIAL_SCREEN_HEIGHT, INITIAL_VILLAGER_COUNT, WINDOW_CAPTION
from pt.villager import Villager


def initialize_components():
    """
    Initializes all components required for the game.

    Returns:
        tuple: A tuple containing the screen, LLM client, and villagers.
    """
    screen = initialize_pygame()
    client = initialize_llm()
    villagers = initialize_villagers()
    return screen, client, villagers


def initialize_pygame():
    """
    Initializes Pygame and sets up the display window.

    Returns:
        pygame.Surface: The screen surface created by Pygame.
    """
    pygame.init()
    screen = pygame.display.set_mode((INITIAL_SCREEN_WIDTH, INITIAL_SCREEN_HEIGHT), pygame.RESIZABLE | pygame.DOUBLEBUF)
    pygame.display.set_caption(WINDOW_CAPTION)
    return screen


def initialize_villagers():
    """
    Initializes a list of villagers.

    Returns:
        list: A list of Villager instances.
    """
    with open('static/first-names.txt', 'r', encoding='utf-8') as names_file:
        with open('static/evil-personality-traits.txt', 'r', encoding='utf-8') as traits_file:
            names = names_file.read().splitlines()
            traits = traits_file.read().splitlines()
            return [
                Villager(
                    INITIAL_SCREEN_WIDTH,
                    INITIAL_SCREEN_HEIGHT,
                    random.choice(names),
                    [random.choice(traits) for _ in range(3)]
                ) for _ in range(INITIAL_VILLAGER_COUNT)
            ]


def initialize_llm():
    """
    Initializes the LLM client.

    Returns:
        openai.OpenAI: The OpenAI client instance.
    """
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("API key for OpenAI is not set.")

    client = openai.OpenAI()
    client.api_key = api_key
    return client
