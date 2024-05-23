import pygame

# CUSTOM MODULES
from src.utils import constants as const

from pygame.time import Clock

# TYPES
from pygame.surface import Surface


class Renderer:
    screen_width: int
    screen_height: int
    fps: int
    screen: Surface
    clock: Clock
    ticks: int

    def __init__(self, screen_width: int, screen_height: int, fps: int):
        self.screen_width = (
            screen_width
            if screen_width > const.SCREEN_WIDTH_MIN
            else const.SCREEN_WIDTH_MIN
        )
        self.screen_height = (
            screen_height
            if screen_height > const.SCREEN_HEIGHT_MIN
            else const.SCREEN_HEIGHT_MIN
        )
        self.fps = fps
        self.ticks = 0

        self.setup()

    def setup(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = Clock()

    def render(self, *scenes) -> None:
        self.fill_screen(255, 255, 255)

        for scene in scenes:
            scene.render()

        pygame.display.flip()
        self.ticks += self.clock.tick(self.fps)

    def fill_screen(self, r: int, g: int, b:int) -> None:
        self.screen.fill((r, g, b))
