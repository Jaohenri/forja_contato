"""Module for Game and Person classes."""

class Entity:
    """Represents an entity in the system.

    Attributes:
            name (str): Represents the name of the entity.    
    """
    def __init__(self, name: str) -> None:
        """Initializes a entity instance.

        Args:
            name (str): Represents the name of the entity.

        """
        self.name = name
        self.active = True

    def set_active(self,active: bool) -> None:
        """Sets the active state of the entity.

        Args:
            active (bool): Indicate if the entity is active, or not.

        """
        self.active = active

    def is_active(self) -> bool:
        """Returns either if the entity is active, or not."""
        return self.active

class Game(Entity):
    """Represents a game, which is an entity in the system.

    Atributes:
            name (str): Name of the game.
            synopsis (str): A short description of the game.
            genre (str): Genre of the game.
            platform (str): Platforms in which the game is available.
            engine (str): Engine running in the game.
            status (str): If the game is active, or not.
    """

    def __init__(self, name: str, synopsis: str,
                 genre: str, platform: str,
                 engine: str, status: str) -> None:
        """Initializes a game instance.

        Args:
            name (str): Name of the game.
            synopsis (str): A short description of the game.
            genre (str): Genre of the game.
            platform (str): Platforms in which the game is available.
            engine (str): Engine running in the game.
            status (str): If the game is active, or not.
        """
        super().__init__(name)
        self.synopsis = synopsis
        self.genre = genre
        self.platform = platform
        self.engine = engine
        self.status = status

class Person(Entity):
    """Represents a person, which is an entity in the system.
    
    Atributes:
            name (str): Name of the person.
            email (str): E-mail address of the person.
            address (str): Address of the person.
            position (str): Occupation of the person in the game sudio.  
    """
    def __init__(self, name: str, email: str, address: str, position: str) -> None:
        """Initializes a person instance.

        Args:
            name (str): Name of the person.
            email (str): E-mail address of the person.
            address (str): Address of the person.
            position (str): Occupation of the person in the game sudio.

        """
        super().__init__(name)
        self.email = email
        self.address = address
        self.position = position
        self.ability_list: list[str] = []

    def add_ability(self, ability: str) -> None:
        """Adds na ability to the ability list if the person doesn't already have this ability.

        Args:
            ability (str): Ability to be added to the ability list.

        Raises:
            ValueError: If the person already has the specified ability.
        """
        if ability.lower() in self.ability_list:
            raise ValueError("This person already has this ability")
        self.ability_list.append(ability.lower())
