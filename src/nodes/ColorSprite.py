from pygame import draw
from src.utils import constants as const

# BASES
from src.bases.Node import Node
from src.bases.Renderable import Renderable

# TYPES
from pygame.surface import Surface
from src.bases.Scene import Scene


class ColorSprite(Node, Renderable):
    scene: Scene
    x: int
    y: int
    width: int
    height: int
    r: int
    g: int
    b: int
    rect_mode: int

    sprite: Surface
    tiles_x: int
    tiles_y: int

    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        width: int,
        height: int,
        r: int,
        g: int,
        b: int,
        rect_mode: int = const.CORNER,
    ):
        super().__init__(scene, x, y, width, height)
        self.r = r
        self.g = g
        self.b = b
        self.rect_mode = rect_mode

        self.rect_mode_setup()

    def rect_mode_setup(self) -> None:
        match self.rect_mode:
            case const.CORNER:
                pass

            case const.CENTER:
                self.x -= self.width // 2
                self.y -= self.height // 2
                self.rect.topleft = (self.x, self.y)

    def render(self) -> None:
        draw.rect(self.scene.renderer.screen, (self.r, self.g, self.b), self.rect)
