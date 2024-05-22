import pygame


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
