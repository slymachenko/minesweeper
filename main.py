from src.core.Core import Core
from src.scenes.PlayScene import PlayScene


def main():
    screen_width: int = 1280
    screen_height: int = 720
    fps: int = 60
    caption = "Minesweeper - by slymachenko"
    icon_path = "assets/imgs/icon.png"
    # music_path = "assets/sounds/music.mp3"

    game = Core(PlayScene, screen_width, screen_height, fps)
    
    game.setup_caption(caption)
    game.setup_icon(icon_path)
    # game.setup_music(music_path)
    
    game.run()


if __name__ == "__main__":
    main()
