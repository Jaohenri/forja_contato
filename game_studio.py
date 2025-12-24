from game import Game

class GameStudio:
    def __init__(self, name: str, link: str) -> None:
        self.name = name
        self.link = link
        self.__gamelist = []
        self.__active = True

    def add_game(self, game: Game) -> None:
        self.__gamelist.append(game)

    def list_games(self) -> list:
        return self.__gamelist
    
    def set_active(self, active: bool) -> None:
        self.__active = active