from pygame import mouse
from src.utils import constants as const

# BASES
from src.bases.nodes.AnimatedSprite import AnimatedSprite

# TYPES
from src.bases.scenes.Scene import Scene


class SmileButton(AnimatedSprite):
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
        super().__init__(scene, x, y, width, height, path, 5, rect_mode, wrap_mode)

    def input(self) -> None:
        mouse_pos = mouse.get_pos()
        
        if self.rect.collidepoint(mouse_pos):
            if self.scene.input_manager.events["l_mouse_down"]:
                self.update_frame(1)
                self.animate()
            
            if self.scene.input_manager.events["l_mouse_up"]:
                self.scene.updater.switch_scene("PlayScene")