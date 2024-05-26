from pygame import error as pygame_error
from pygame import mixer
from pygame import quit
from pygame.image import load
from pygame.display import set_caption
from pygame.display import set_icon

from src.core.InputManager import InputManager
from src.core.Updater import Updater
from src.core.Renderer import Renderer

# TYPES
from src.bases.Scene import Scene


class Core:
    screen_width: int
    screen_height: int
    fps: int

    input_manager: InputManager
    updater: Updater
    renderer: Renderer

    current_scene: Scene

    def __init__(
        self,
        start_scene: Scene,
        screen_width: int = 1280,
        screen_height: int = 720,
        fps: int = 60,
    ):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.fps = fps

        self.input_manager = InputManager(self)
        self.updater = Updater(self)
        self.renderer = Renderer(self.screen_width, self.screen_height, self.fps)

        self.current_scene = start_scene(
            self.input_manager, self.updater, self.renderer
        )

    def setup_caption(self, caption: str) -> None:
        set_caption(caption)
    
    def setup_icon(self, icon_path: str) -> None:
        try:
            set_icon(load(icon_path))
        except FileNotFoundError:
            print("Icon setup failed")

    def setup_music(self, music_path: str) -> None:
        try:
            mixer.init()
            mixer.music.load(music_path)
            mixer.music.set_volume(0.2)
            mixer.music.play(-1)
        except pygame_error:
            print("Music setup failed")

    def switch_scene(self, new_scene: Scene) -> None:
        self.current_scene = new_scene(self.input_manager, self.updater, self.renderer)

    def run(self) -> None:
        while self.updater.is_game_running:
            self.input_manager.input((self.current_scene))
            self.updater.update((self.current_scene))
            self.renderer.render((self.current_scene))

        quit()
