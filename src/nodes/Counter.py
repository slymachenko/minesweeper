# TYPES
from src.bases.Node import Node
from src.bases.Scene import Scene
from src.nodes.AnimatedSprite import AnimatedSprite

class Counter(Node):
    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        path: str,
        digits: int,
    ):
        width = 13 * digits
        height = 23
        super().__init__(scene, x, y, width, height)

        self.path = path
        self.digits = digits

        self.nodes = []

        self.gen_digits()
    
    def gen_digits(self):
        for i in range(self.digits):
            self.nodes.append(
                AnimatedSprite(
                    self.scene,
                    self.x + i * 13,
                    self.y,
                    13,
                    23,
                    self.path,
                    11),
            )
    
    def update_digits(self, number: int):
        digits = [int(d) for d in str(number).zfill(self.digits)]
        
        for i in range(len(digits)):
            self.nodes[i].update_frame(digits[i])
            self.nodes[i].animate()