from pygame import mouse
from src.utils import constants as const

# BASES
from src.bases.nodes.Sprite import Sprite

# TYPES
from src.bases.scenes.Scene import Scene


class Cell(Sprite):
    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        width: int,
        height: int,
        path: str,
        rect_mode: int = const.CORNER,
        wrap_mode: int = const.CLAMP,
    ):
        super().__init__(scene, x, y, width, height, path, rect_mode, wrap_mode)

    def input(self) -> None:
        if self.scene.input_manager.events["click"]:
            mouse_pos = mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                print("Cell clicked!")
