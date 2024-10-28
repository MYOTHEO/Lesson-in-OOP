#abstraction
from abc import ABC, abstractmethod
class Character(ABC):
    def __init__(self, name):
        super().__init__()
        self.name = name
    @abstractmethod
    def special_move(self):
        pass
class MainCharacter(Character):
    def special_move(self, move):
        print(f"{self.name} use the special move {move}")
        
dbz = MainCharacter("Vegeta")
dbz.special_move("Final Flash")