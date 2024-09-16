class Hero():
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def describeHero(self):
            print(f"Brand: {self.name} has {self.health}")
    
class Marksman(Hero):
    def __init__(self, name, health, long_range):
        super().__init__(name, health)
        self.long_range = long_range
    def has_first_blood(self):
        print(f"{self.name} has First Blood!")

miya = Marksman("Miya","200","Malayuang Barilan")
miya.has_first_blood()