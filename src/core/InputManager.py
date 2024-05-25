import pygame

# KEYBOARD KEYS
from pygame.locals import K_e


class InputManager:
    events: dict[str:int]

    def __init__(self, core):
        self.core = core
        self.l_mouse_button_down = False

    def input(self, *scenes) -> None:
        self.events = {
            "l_mouse_up": 0, 
            "r_mouse_up": 0, 
            "l_mouse_down": 0
        }

        # Mouse handling
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    self.core.updater.quit()
                case pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.events["l_mouse_down"] = 1
                        self.l_mouse_button_down = True
                case pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.events["l_mouse_up"] = 1
                        self.l_mouse_button_down = False
                    if event.button == 3:
                        self.events["r_mouse_up"] = 1

        # Keyboard handling
        keys: list[int] = pygame.key.get_pressed()

        if keys[K_e]:
            self.events["e"] = 1
        
        # Call input for each node
        for scene in scenes:
            scene.input()
