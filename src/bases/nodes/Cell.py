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
        super().__init__(scene, x, y, width, height, path, 14, rect_mode, wrap_mode)
        self.is_blocked: bool = False
        self.is_revealed: bool = False
        self.is_clicked: bool = False
        self.is_flagged: bool = False
        self.value: int = -1 if is_mine else 0

    def input(self) -> None:
        if self.is_blocked:
            return

        if self.scene.input_manager.events["click"]:
            mouse_pos = mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.is_clicked = True
                if self.value == -1:
                    self.scene.game_over()
                self.reveal()
        
        if self.scene.input_manager.events["r_click"]:
            mouse_pos = mouse.get_pos()
            if self.rect.collidepoint(mouse_pos):
                self.toggle_flag()

    def reveal(self):
        if self.is_revealed or self.is_flagged and self.value != -1:
            return
        self.is_revealed = True

        # Update adjacent cells
        for cell in self.scene.grid.get_adjacent_cells(self):
            if cell.value == -1 and self.value != -1:
                self.value += 1

        match self.value:
            case -1:
                if self.is_clicked:
                    self.update_frame(12)
                elif self.is_flagged:
                    self.update_frame(13)
                else:
                    self.update_frame(11)

                self.scene.grid.reveal_all_mines()
                self.scene.grid.block_all_cells()
            case 0:
                self.update_frame(9)
                self.scene.grid.update_hidden_cells()

                for cell in self.scene.grid.get_adjacent_cells(self):
                    if cell.value != -1:
                        cell.reveal()
        
        if 1 <= self.value and self.value <= 8:
            self.update_frame(self.value)
            self.scene.grid.update_hidden_cells()
        
        self.animate()
    
    def toggle_flag(self):
        self.is_flagged = not self.is_flagged

        self.scene.flag_counter.flags += 1 if not self.is_flagged else -1      
        self.scene.flag_counter.update_digits(self.scene.flag_counter.flags)

        self.update_frame(10) if self.is_flagged else self.update_frame(0)
        self.animate()