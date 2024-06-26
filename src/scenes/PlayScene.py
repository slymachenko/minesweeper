import random
from src.utils import constants as const

from src.nodes.ColorSprite import ColorSprite
from src.nodes.Sprite import Sprite
from src.nodes.Grid import Grid
from src.nodes.Counter import Counter
from src.nodes.Timer import Timer
from src.nodes.SmileButton import SmileButton

# BASES
from src.bases.Scene import Scene

# TYPES
from src.bases.Node import Node
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

        self.setup()

    def setup(self) -> None:
        # Generate nodes
        self.gen_bg()

        self.gen_play_zone()

        self.gen_grid()

        self.gen_header()
    
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
            self.updater.game_screen_x[0],
            (self.updater.game_screen_x[1]) // 16 * 16,
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
        self.grid = Grid(
            self,
            self.updater.game_screen_x[0] + 32, 
            self.updater.game_screen_y[0] + 32 + 25 + 75, 
            self.updater.game_screen_x[1] - 64,
            self.updater.game_screen_y[1] - 64 - 50 - 75,
            0.1)
        
        self.nodes += self.grid.nodes

    def gen_header(self) -> None:
        header_zone = ((
            self.updater.game_screen_x[0] + 25,
            self.updater.game_screen_x[1] - 50
        ),(
            self.updater.game_screen_y[0] + 50,
            50,
        ))


        self.nodes.append(
            Sprite(
                self,
                header_zone[0][0],
                header_zone[1][0],
                header_zone[0][1],
                header_zone[1][1],
                "assets/imgs/header.png",
                wrap_mode=const.STRETCH),
        )

        self.gen_smile_button()
        self.gen_flag_counter()
        self.gen_timer()
    
    def gen_smile_button(self) -> None:
        self.smile_button = SmileButton(
            self,
            self.updater.game_screen_x[0] + self.updater.game_screen_x[1] // 2,
            self.updater.game_screen_y[0] + 62,
            24,
            24,
            "assets/imgs/smiles.png",
            wrap_mode=const.CLAMP)

        self.nodes.append(self.smile_button)

    def gen_flag_counter(self) -> None:
        self.flag_counter = Counter(
            self,
            self.updater.game_screen_x[0] + 50,
            self.updater.game_screen_y[0] + 62,
            "assets/imgs/scores.png",
            3,
        )

        self.flag_counter.flags = self.grid.mines
        self.flag_counter.update_digits(self.flag_counter.flags)
        
        self.nodes += self.flag_counter.nodes

    def gen_timer(self) -> None:
        self.timer = Timer(
            self,
            self.updater.game_screen_x[1] - 50 + (self.renderer.screen_width - self.renderer.screen_height) // 2 - 39,
            self.updater.game_screen_y[0] + 62,
            "assets/imgs/scores.png",
            3,
        )
        
        self.nodes += self.timer.nodes

    def game_over(self, is_lost: bool = True) -> None:
        if is_lost:
            self.smile_button.update_frame(4)
            self.smile_button.animate()
            self.timer.stop()
        else:
            self.smile_button.update_frame(3)
            self.smile_button.animate()
            self.timer.stop()
    
    def update(self) -> None:
        if self.timer.is_running:
            self.timer.run()