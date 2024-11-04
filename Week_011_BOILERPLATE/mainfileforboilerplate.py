from abc import ABC, abstractmethod

class Ibon(ABC):
    def __init__(self, name):
        self.name = name

    @property #abstract property
    @abstractmethod
    def lumilipad(self):
        pass

class Kalapati(Ibon):
    @property #abstract property
    def lumilipad(self):
        return f"Ang {self.name} ay marunong lumipad!"

if __name__ == "__main__":
    print("boi")