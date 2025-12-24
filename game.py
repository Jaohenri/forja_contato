"""Module for Game and Person classes."""

class Entity:
    """
    Represents a Entity in the system.

    Attributes:
    name (str): Name of the Entity
    active (bool): Status of the Entity

    Methods:
    set_active(active: bool) -> None: Sets the active status of the Entity
    is_active() -> bool: Returns the active status of the Entity
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.active = True

    def set_active(self,active: bool) -> None:
        self.active = active

    def is_active(self) -> bool:
        return self.active

class Game(Entity):

    def __init__(self, name: str, synopsis: str,
                 genre: str, platform: str,
                 engine: str, status: str) -> None:
        super().__init__(name)
        self.synopsis = synopsis
        self.genre = genre
        self.platform = platform
        self.engine = engine
        self.status = status

class Person(Entity):
    """
    Docstring for Person
    """
    def __init__(self, name: str, email: str, address: str, position: str) -> None:
        super().__init__(name)
        self.email = email
        self.address = address
        self.position = position
