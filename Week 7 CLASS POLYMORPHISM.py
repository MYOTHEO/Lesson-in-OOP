class Marksman:
    def __init__(self, name, atk_dmg):
        self.name = name
        self.atk_dmg = atk_dmg
        
    def describeHero(self):
        print(self.name, self.atk_dmg)
        
class Tank:
    def __init__(self, name, armor):
        self.name = name
        self.armor = armor
        
    def describeHero(self):
        print(self.name, self.armor)

class Assassin:
    def __init__(self, name, penetration):
        self.name = name
        self.atk_dmg = penetration
        
    def describeHero(self):
        print(self.name, self.atk_dmg)
        
layla = Marksman("Layla", 290)
johnson = Tank("Johnson", "Athena's Shield")
ling = Assassin("Ling", "Malefic Roar")

for hero in [layla, johnson, ling]:
    hero.describeHero()