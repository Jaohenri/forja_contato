"""Module for test the implementation of the Game, Person and GameStudio classes."""

from game import Game, Person
from game_studio import GameStudio

if __name__ == "__main__":
    game1 = Game("The last of us", "Zombies", "Action", "Playstation", "Unreal", "active")
    game2 = Game("The last of us 2", "Zombies", "Action", "Playstation", "Unreal", "active")
    game_studio = GameStudio("CD PROJEKT RED", "TEST")
    game_studio.add_game(game1)
    game_studio.add_game(game2)
    print(game_studio.list_games())

    person1 = Person("João", "joao123@gmail,com", "Rua 123", "Intern")
    person1.add_ability("Read")
    print(person1.list_abilities())
    print(person1)
