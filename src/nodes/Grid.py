import random
from src.nodes.Cell import Cell

# TYPES
from src.bases.Node import Node
from src.bases.Scene import Scene


class Grid(Node):
    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        width: int,
        height: int,
        mines_percentage: int
    ):
        super().__init__(scene, x, y, width, height)
        self.tiles = (self.width // 16, self.height // 16)
        self.mines = (int)(mines_percentage * self.tiles[0] * self.tiles[1])
        
        self.nodes = []
        self.hidden_cells = self.tiles[0] * self.tiles[1] - self.mines
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
                random.randrange(1, self.tiles[0]),
                random.randrange(1, self.tiles[1]),
            ]

            if rand_pos not in self.mines_positions: 
                self.mines_positions.append(rand_pos)
                mines_amount -= 1
    
    def gen_grid(self):
        for i in range(self.tiles[0]):
            for j in range(self.tiles[1]):
                self.nodes.append(
                    Cell(
                        self.scene,
                        self.x + i * (self.width // self.tiles[0]),
                        self.y + j * (self.height // self.tiles[1]),
                        self.width // self.tiles[0],
                        self.height // self.tiles[1],
                        "assets/imgs/cells.png",
                        True if [i, j] in self.mines_positions else False
                    ),
                )
    
    def get_adjacent_cells(self, cell):
        adjacent_cells = []
        index = self.nodes.index(cell)

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                x, y = index // self.tiles[1] + dx, index % self.tiles[1] + dy
                if 0 <= x < self.tiles[0] and 0 <= y < self.tiles[1]:
                    adjacent_cells.append(self.nodes[x * self.tiles[1] + y])

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