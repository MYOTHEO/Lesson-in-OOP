class Hero():
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def describeHero(self):
            print(f"Brand: {self.name} has {self.health}")
    
class Marksman(Hero):
    def __init__(self, name, health):
        super().__init__(name, health)

miya = Marksman("Miya","200")
miya.describeHero()