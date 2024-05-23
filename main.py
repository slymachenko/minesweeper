from src.core.Core import Core
from src.scenes.PlayScene import PlayScene


def main():
    screen_width: int = 1280
    screen_height: int = 720
    fps: int = 60

    game = Core(PlayScene, screen_width, screen_height, fps)
    game.run()


if __name__ == "__main__":
    main()
