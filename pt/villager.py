import random
import pygame

from typing import Optional

from pt.config import SPEED_SLIDER_ENABLED



DEFAULT_SPEED_FACTOR = 2


class Villager:
    """
    Represents a single villager.

    Attributes:
        position (tuple[float, float]): the x-, y- cordinates of the villager.
        velocity (tuple[float, float]): the velocity along the x, y axis.
    """

    tokens_used = 0
    last_interaction = 0

    def __init__(
            self,
            screen_width: int,
            screen_height: int,
            name: str,
            personality_traits: list[str],
            speed_factor: Optional[int] = None
    ) -> None:  
        # TODO pylint is somewhat correct by too many arguments - e.g. we can get screen width/height smarter-er with screen.get_size()
        # TODO make it so pylint doesn't give this warning
        self.x_boundary = screen_width
        self.y_boundary = screen_height
        self.name = name
        self.personality_traits = personality_traits
        self.speed = speed_factor if speed_factor else DEFAULT_SPEED_FACTOR

        self.set_position(random.randint(0, self.x_boundary), random.randint(0, self.y_boundary))
        self.velocity = pygame.math.Vector2(
            random.uniform(-1, 1) * self.speed,
            random.uniform(-1, 1) * self.speed
        )

    def set_position(self, x: float, y: float) -> None:
        """
        Sets the villager's position.
        
        Args:
            x (float): The new x-coordinate.
            y (float): The new y-coordinate.
        """
        self.position = pygame.math.Vector2(x, y)

    def update_position(self, screen_width: int, screen_height: int) -> None:
        """
        Updates the villager's position based on its velocity and the current screen dimensions.
        
        Args:
            screen_width (int): The current width of the screen.
            screen_height (int): The current height of the screen.
        """

        self.position += self.velocity

        # Bounce off the walls and ensure villagers stay within boundaries
        if self.position.x < 0:
            self.position.x = 0
            self.velocity.x = -self.velocity.x
        elif self.position.x > screen_width:
            self.position.x = screen_width
            self.velocity.x = -self.velocity.x

        if self.position.y < 0:
            self.position.y = 0
            self.velocity.y = -self.velocity.y
        elif self.position.y > screen_height:
            self.position.y = screen_height
            self.velocity.y = -self.velocity.y

    def update_speed(self, new_speed: float) -> None:
        """
        Updates the villager's speed and adjusts the velocity accordingly.
        
        Args:
            new_speed (float): The new speed factor.
        """
        self.speed = new_speed
        self.velocity = self.velocity.normalize() * self.speed


def update_villagers(villagers: list[Villager], new_speed, screen_width: int, screen_height: int):
    """
    Updates all villagers in the simulation.

    Args:
        villagers (list): A list of Villager instances.
        new_speed (float): The new speed factor.
        screen_width (int): The current width of the screen.
        screen_height (int): The current height of the screen.
    """
    for villager in villagers:
        villager.update_position(screen_width, screen_height)
        if SPEED_SLIDER_ENABLED:  # TODO this is bad for scalability and also it hurts my heart
            villager.update_speed(new_speed)
