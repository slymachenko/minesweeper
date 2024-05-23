import random
from src.bases.nodes.Cell import Cell

# TYPES
from src.bases.nodes.Node import Node
from src.bases.scenes.Scene import Scene


class Grid(Node):
    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        width: int,
        height: int,
        tiles: int,
        mines_percentage: int
    ):
        super().__init__(scene, x, y, width, height)
        self.tiles = tiles
        self.mines = mines_percentage * tiles * tiles
        
        self.nodes = []
        self.setup()
    
    def setup(self):
        self.gen_mines_positions()
        self.gen_grid()

    def gen_mines_positions(self):
        # Mines generation
        mines_amount = self.mines
        self.mines_positions = []
        while mines_amount > 0:
            rand_pos = [
                random.randrange(1, self.tiles),
                random.randrange(1, self.tiles),
            ]

            if rand_pos not in self.mines_positions: 
                self.mines_positions.append(rand_pos)
                mines_amount -= 1
    
    def gen_grid(self):
        # grid_panel = ((
        #     self.scene.updater.game_screen_x[0] + 32 + 25,
        #     (self.scene.updater.game_screen_x[1] - 64 - 50) // self.tiles,
        # ),(
        #     self.scene.updater.game_screen_y[0] + 32 + 25,
        #     (self.scene.updater.game_screen_y[1] - 64 - 50) // self.tiles,
        # ))

        for i in range(self.tiles):
            for j in range(self.tiles):
                self.nodes.append(
                    Cell(
                        self.scene,
                        self.x + i * self.width,
                        self.y + j * self.height,
                        self.width,
                        self.height,
                        "assets/imgs/cells.png",
                        True if [i, j] in self.mines_positions else False
                    ),
                )        