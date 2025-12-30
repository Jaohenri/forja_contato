from game import Game
from game_studio import GameStudio

if __name__ == "__main__":
    game1 = Game("The last of us", "Zombies and Families", "Action", "Playstation", "Unreal", "active")
    game_studio = GameStudio("CD PROJEKT RED", "TEST")
    game_studio.add_game(game1)
    print(game_studio.list_games())