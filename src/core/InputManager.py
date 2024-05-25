import pygame

# KEYBOARD KEYS
from pygame.locals import K_e


class InputManager:
    events: dict[str:int]

    def __init__(self, core):
        self.core = core

    def input(self, *scenes) -> None:
        self.events = {"click": 0, "r_click": 0, "e": 0}

        # Mouse handling
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.core.updater.quit()
                case pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.events["click"] = 1
                    if event.button == 3:
                        self.events["r_click"] = 1

        # Keyboard handling
        keys: list[int] = pygame.key.get_pressed()

        if keys[K_e]:
            self.events["e"] = 1
        
        # Call input for each node
        for scene in scenes:
            scene.input()
