import random
from src.utils import constants as const

from src.bases.nodes.ColorSprite import ColorSprite
from src.bases.nodes.Sprite import Sprite
from src.bases.nodes.Grid import Grid

# BASES
from src.bases.scenes.Scene import Scene

# TYPES
from src.bases.nodes.Node import Node
from src.core.InputManager import InputManager
from src.core.Updater import Updater
from src.core.Renderer import Renderer


class PlayScene(Scene):
    nodes: list[Node]

    def __init__(
        self, input_manager: InputManager, updater: Updater, renderer: Renderer
    ):
        self.input_manager = input_manager
        self.updater = updater
        self.renderer = renderer
        self.nodes = list()

        tiles = 16
        self.grid = Grid(
            self,
            self.updater.game_screen_x[0] + 32 + 25, 
            self.updater.game_screen_y[0] + 32 + 25, 
            (self.updater.game_screen_x[1] - 64 - 50) // tiles,
            (self.updater.game_screen_y[1] - 64 - 50) // tiles,
            16,
            0.1)
        self.setup()

    def setup(self) -> None:
        # Generate nodes
        self.gen_bg()

        self.gen_play_zone()

        self.gen_grid()
    
    def gen_bg(self) -> None:
        self.nodes.append(
            ColorSprite(
                self,
                0,
                0,
                self.renderer.screen_width,
                self.renderer.screen_height,
                130, 128, 128)
        )
    
    def gen_play_zone(self) -> None:
        play_zone = ((
            self.updater.game_screen_x[0] + 25,
            (self.updater.game_screen_x[1] - 50) // 16 * 16,
        ),(
            self.updater.game_screen_y[0] + 25,
            (self.updater.game_screen_y[1] - 50) // 16 * 16,
        ))

        self.nodes.append(
            Sprite(
                self,
                play_zone[0][0],
                play_zone[1][0],
                play_zone[0][1],
                16,
                "assets/imgs/play_zone_outer_border_top.png",
                wrap_mode=const.STRETCH),
        )

        self.nodes.append(
            Sprite(
                self,
                play_zone[0][0],
                play_zone[1][0],
                16,
                play_zone[1][1],
                "assets/imgs/play_zone_outer_border_left.png",
                wrap_mode=const.STRETCH),
        )

        self.nodes.append(
            Sprite(
                self,
                play_zone[0][0],
                play_zone[1][0],
                16,
                16,
                "assets/imgs/play_zone_outer_border_corner.png",
                wrap_mode=const.STRETCH),
        )

        self.nodes.append(
            ColorSprite(
                self,
                play_zone[0][0] + 16,
                play_zone[1][0] + 16,
                play_zone[0][1] - 16,
                play_zone[1][1] - 16,
                192, 192, 192),
        )
    
    def gen_grid(self) -> None:
        self.nodes += self.grid.nodes