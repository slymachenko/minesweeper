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

        self.setup()

    def setup(self) -> None:
        pass