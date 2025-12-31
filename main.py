from game import Game, Person
from game_studio import GameStudio

if __name__ == "__main__":
    game1 = Game("The last of us", "Zombies and Families", "Action", "Playstation", "Unreal", "active")
    game_studio = GameStudio("CD PROJEKT RED", "TEST")
    game_studio.add_game(game1)
    print(game_studio.list_games())

    """person1 = Person("João", "joao123@gmail,com", "Rua 123", "Intern")
    person1.add_ability("Read")
    print(person1.list_abilities())
    print(person1)"""