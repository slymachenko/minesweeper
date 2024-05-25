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
        self.mines = (int)(mines_percentage * tiles * tiles)
        
        self.nodes = []
        self.hidden_cells = tiles * tiles - self.mines
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
    
    def get_adjacent_cells(self, cell):
        adjacent_cells = []
        index = self.nodes.index(cell)

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                x, y = index % self.tiles + dx, index // self.tiles + dy
                if 0 <= x < self.tiles and 0 <= y < self.tiles:
                    adjacent_cells.append(self.nodes[y * self.tiles + x])

        return adjacent_cells

    def reveal_all_mines(self):
        for node in self.nodes:
            if node.value == -1:
                node.reveal()
    
    def block_all_cells(self):
        for node in self.nodes:
            node.is_blocked = True
    
    def update_hidden_cells(self):
        self.hidden_cells -= 1
        if self.hidden_cells <= 0:
            self.scene.game_over(False)
            self.reveal_all_mines()
            self.block_all_cells()