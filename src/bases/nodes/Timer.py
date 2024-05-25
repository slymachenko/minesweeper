# TYPES
from src.bases.nodes.Counter import Counter
from src.bases.scenes.Scene import Scene

class Timer(Counter):
    def __init__(
        self,
        scene: Scene,
        x: int,
        y: int,
        path: str,
        digits: int,
    ):
        super().__init__(scene, x, y, path, digits)

        self.seconds = 0
        self.is_running = True
        self.step_timer = self.scene.renderer.ticks

    def run(self):
        if self.seconds >= 999:
            self.stop()
            return self.scene.game_over()

        now = self.scene.renderer.ticks
        if now - self.step_timer > 1000:
            self.step_timer = now
            self.seconds += 1

            self.update_digits(self.seconds)
    
    def stop(self):
        self.is_running = False