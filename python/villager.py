import random
import pygame

from typing import Optional



DEFAULT_SPEED_FACTOR = 2


class Villager:
    """
    Represents a single villager.

    Attributes:
        position (tuple[float, float]): the x-, y- cordinates of the villager.
        velocity (tuple[float, float]): the velocity along the x, y axis.
    """

    def __init__(
            self,
            screen_width: int,
            screen_height: int,
            speed_factor: Optional[int] = None
    ) -> None:
        self.x_boundary = screen_width
        self.y_boundary = screen_height
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
