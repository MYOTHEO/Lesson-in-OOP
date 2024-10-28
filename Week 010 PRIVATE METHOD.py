#Private Method
class Bday:
    def __init__(self, name):
        self.name = name 
        
    def __lumpia(self):
        print(f"Lumpiang {self.name}") 
    def handaan(self):
        print(f"Cake, Lechon, Spag") 
        self.__lumpia()
            
shanghai = Bday("Shanghai")
shanghai.handaan()