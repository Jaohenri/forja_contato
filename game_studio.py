"""Module for game studios."""
from game import Game

class GameStudio:
    """Represents a game studio in the system.
    
    Attributes:
            name (str): Name of the game studio.
            link (str): Link to the game studio.
    """
    def __init__(self, name: str, link: str) -> None:
        """Initializes a game studio instance in the system.

        Args:
            name (str): Name of the game studio.
            link (str): Link to the game studio.
        """
        self.name = name
        self.link = link
        self.__gamelist: list[Game] = []
        self.__active = True

    def add_game(self, game: Game) -> None:
        """Adds a game to the game list of the game studio.

        Args:
            game (Game): Represents a game instance.
        """
        self.__gamelist.append(game)

    def list_games(self) -> list[Game]:
        """Lists all the games of the game studio.

        Returns:
            list: A list of the game studio's games.
        """
        return self.__gamelist

    def set_active(self, active: bool) -> None:
        """Sets the active state of the game studio.

        Args:
            active (bool): Indicate if the game studio is active, or not.

        """
        self.__active = active

    def is_active(self) -> bool:
        """Checks whether the game studio is active.

        Returns:
            bool: True if the studio is active, False otherwise.
        """
        return self.__active
