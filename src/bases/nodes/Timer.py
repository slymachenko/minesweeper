# TYPES
from src.bases.nodes.Node import Node
from src.bases.scenes.Scene import Scene
from src.bases.nodes.AnimatedSprite import AnimatedSprite

class Timer(Node):
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

        self.seconds = 0
        self.nodes = []
        self.is_running = True

        self.setup()

    def setup(self):
        self.step_timer = self.scene.renderer.ticks
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

    def run(self):
        if self.seconds >= 999:
            self.stop()
            return self.scene.game_over()

        now = self.scene.renderer.ticks
        if now - self.step_timer > 1000:
            self.step_timer = now
            self.seconds += 1

            self.update_digits()
    
    def update_digits(self):
        digits = [int(d) for d in str(self.seconds).zfill(self.digits)]
        
        for i in range(len(digits)):
            self.nodes[i].update_frame(digits[i])
            self.nodes[i].animate()
    
    def stop(self):
        self.is_running = False