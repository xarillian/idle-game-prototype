import pygame


# TODO these ui elements need to be cleaned up badly after we hit MVP status
# TODO we can use screen size more effectively, again
# TODO these are really tightly coupled


class DebugMenu:
    """
    Represents a debug menu with multiple checkboxes.

    Attributes:
        screen (pygame.Surface): The screen on which to render the debug menu.
        checkboxes (list[Checkbox]): A list of checkboxes in the debug menu.
    """

    def __init__(self, screen, screen_height):
        self.screen = screen
        self.checkboxes = [
            Checkbox(screen, 10, 40, 10, 10, ''),
            Checkbox(screen, 10, 20, 10, 10, 'Speed Slider')
        ]
        self.update_positions(screen_height)

    def render(self):
        """ Renders the debug menu on the screen. """
        for checkbox in self.checkboxes:
            checkbox.render()

    def handle_event(self, event):
        """
        Handles events for the debug menu.

        Args:
            event (pygame.event.Event): The event to handle.
        """
        for checkbox in self.checkboxes:
            checkbox.handle_event(event)

    def is_speed_slider_checked(self):
        """ Returns whether the speed slider checkbox is checked. """
        return self.checkboxes[1].checked

    def update_positions(self, screen_height):
        """
        Updates the positions of all checkboxes based on the current screen dimensions.

        Args:
            screen_width (int): The current width of the screen.
            screen_height (int): The current height of the screen.
        """
        for checkbox in self.checkboxes:
            checkbox.update_position(screen_height)


class Checkbox:
    """
    Represents a checkbox UI element.

    Attributes:
        screen (pygame.Surface): The screen on which to render the checkbox.
        rect (pygame.Rect): The rectangle representing the checkbox.
        checked (bool): Whether the checkbox is checked.
        label (str): The label for the checkbox.
    """

    PADDING_BETWEEN_BOX_AND_LABEL = 5

    def __init__(self, screen, x, y, width, height, label):
        self.screen = screen
        self.offset_x = x
        self.offset_y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.checked = False
        self.label = label

    def render(self):
        """ Renders the checkbox and its label on the screen. """
        pygame.draw.rect(self.screen, (200, 200, 200), self.rect, 2)
        if self.checked:
            pygame.draw.rect(self.screen, (200, 200, 200), self.rect)

        font = pygame.font.Font(None, 18)
        label_surface = font.render(self.label, True, (255, 255, 255))
        self.screen.blit(
            label_surface,
            (self.rect.x + self.rect.width + self.PADDING_BETWEEN_BOX_AND_LABEL, self.rect.y)
        )

    def handle_event(self, event):
        """
        Handles mouse events for the checkbox.

        Args:
            event (pygame.event.Event): The event to handle.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            self.checked = not self.checked

    def update_position(self, screen_height):
        """
        Updates the checkbox position based on the current screen dimensions.

        Args:
            screen_height (int): The current height of the screen.
        """
        self.rect.x = self.offset_x
        self.rect.y = screen_height - self.offset_y


class SpeedSlider:
    """
    Represents a slider to control the speed of villagers.

    Attributes:
        screen (pygame.Surface): The screen on which to render the slider.
        rect (pygame.Rect): The rectangle representing the slider.
        min_speed (float): The minimum speed value.
        max_speed (float): The maximum speed value.
        current_speed (float): The current speed value set by the slider.
        knob_rect (pygame.Rect): The rectangle representing the knob.
        dragging (bool): Whether the knob is being dragged.
    """
    # TODO let's upscope some of the values here

    def __init__(self, screen, screen_width, screen_height, width, height, min_speed, max_speed):
        self.screen = screen
        screen_width, screen_height = screen.get_size()
        self.rect = pygame.Rect(
            (screen_width - width) // 2,
            screen_height - height - 40,
            width,
            height
        )
        self.min_speed = min_speed
        self.max_speed = max_speed
        self.current_speed = (min_speed + max_speed) / 2
        self.knob_rect = pygame.Rect(
            self.rect.x + (self.rect.width - height) // 2,
            self.rect.y,
            height,
            height
        )
        self.dragging = False

    def render(self):
        """ Renders the slider and the current speed value on the screen. """
        pygame.draw.rect(self.screen, (200, 200, 200), self.rect)
        pygame.draw.rect(self.screen, (100, 100, 100), self.knob_rect)

        font = pygame.font.Font(None, 36)
        speed_text = font.render(f"Speed: {self.current_speed:.2f}", True, (255, 255, 255))
        text_rect = speed_text.get_rect(center=(self.rect.centerx, self.rect.y + self.rect.height + 20))
        self.screen.blit(speed_text, text_rect)

    def handle_event(self, event):
        """
        Handles mouse events for the slider.

        Args:
            event (pygame.event.Event): The event to handle.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and self.knob_rect.collidepoint(event.pos):
            self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            new_x = min(max(event.pos[0], self.rect.x), self.rect.x + self.rect.width - self.knob_rect.width)
            self.knob_rect.x = new_x
            self.current_speed = self.min_speed + ((new_x - self.rect.x) / (self.rect.width - self.knob_rect.width)) * (self.max_speed - self.min_speed)
