from src.utils import constants as const

# BASES
from src.nodes.Sprite import Sprite

# TYPES
from typing import Tuple
from pygame.surface import Surface
from src.bases.Scene import Scene


class AnimatedSprite(Sprite):
    num_frames: int

    current_frame: int
    sprite_sheet: Surface
    sprite_size: Tuple[int, int]

    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        width: int,
        height: int,
        path: str,
        num_frames: int,
        rect_mode: int = const.CORNER,
        wrap_mode: int = const.CLAMP,
    ):
        super().__init__(scene, x, y, width, height, path, rect_mode, wrap_mode)
        self.num_frames = num_frames

        self.current_frame = 0
        self.sprite_sheet = self.sprite
        self.animate()

    def update_frame(self, frame: int) -> None:
        self.current_frame = (frame) % self.num_frames

    def animate(self) -> None:
        sprite_size = self.sprite.get_size()
        sprite_sheet_size = self.sprite_sheet.get_size()

        self.sprite = self.sprite_sheet.subsurface(
            self.current_frame * sprite_size[0],
            0,
            sprite_sheet_size[0] // self.num_frames,
            sprite_sheet_size[1],
        )
