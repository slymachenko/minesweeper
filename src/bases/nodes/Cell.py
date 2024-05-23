from pygame import mouse
from src.utils import constants as const

# BASES
from src.bases.nodes.AnimatedSprite import AnimatedSprite

# TYPES
from src.bases.scenes.Scene import Scene


class Cell(AnimatedSprite):
    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        width: int,
        height: int,
        path: str,
        is_mine: bool,
        rect_mode: int = const.CORNER,
        wrap_mode: int = const.CLAMP,
    ):
        super().__init__(scene, x, y, width, height, path, 13, rect_mode, wrap_mode)
        self.is_mine = is_mine
        self.is_revealed = False
        self.is_flagged = False

    def input(self) -> None:
        if self.scene.input_manager.events["click"]:
            mouse_pos = mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.reveal()

    def reveal(self):
        self.revealed = True
        if self.is_mine:
            self.update_frame(12)
        else:
            self.update_frame(self.current_frame + 1)
            self.animate()