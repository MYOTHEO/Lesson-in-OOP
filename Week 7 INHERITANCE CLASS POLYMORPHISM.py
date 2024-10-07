class MOBA:
    def __init__ (self, name, platform):
        self.name = name
        self.platform = platform
        
    def describeMOBA(self):
        print(f"{self.name.upper()}is in platform of {self.platform}")
    
class LeagueOfLegends(MOBA):
    pass
    
class Dota2(MOBA):    
    def __init__(self, name, platform):
        super().__init__(name, platform)
        
class MLBB(MOBA):
    def __init__(self, name, platform):
        MOBA.__init__(self, name, platform)
    def describeMOBA(self):
        print("ok")
    
lol = LeagueOfLegends("LoL", "PC & Mobile")
dota = Dota2("Defence of the acients 2","PC & Steam Deck")
ml = MLBB("Mobile Legends","Android & PC")

lol.describeMOBA()
dota.describeMOBA()
ml.describeMOBA()
