import random


SPEED_FACTOR = 2


class Villager:
    """
    Represents a villager.

    Attributes:
        x (float): The x-coordinate of the villager.
        y (float): The y-coordinate of the villager.
        vx (float): The velocity of the villager along the x-axis.
        vy (float): The velocity of the villager along the y-axis.
    """

    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.x: float = random.randint(0, screen_width)
        self.y: float = random.randint(0, screen_height)
        self.vx: float = random.uniform(-1, 1) * SPEED_FACTOR
        self.vy: float = random.uniform(-1, 1) * SPEED_FACTOR

    def update(self, screen_width: int, screen_height: int):
        """
        Updates the villager's position based on its velocity and the current screen dimensions.
        
        Args:
            screen_width (int): The current width of the screen.
            screen_height (int): The current height of the screen.
        """
        self.x += self.vx
        self.y += self.vy

        if self.x < 0:
            self.x = 0
            self.vx = -self.vx
        elif self.x > screen_width:
            self.x = screen_width
            self.vx = -self.vx

        if self.y < 0:
            self.y = 0
            self.vy = -self.vy
        elif self.y > screen_height:
            self.y = screen_height
            self.vy = -self.vy
