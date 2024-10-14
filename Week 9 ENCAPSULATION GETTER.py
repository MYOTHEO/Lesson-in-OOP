#Encapsulation Getter
class Lumpia_wrapper:
    def __init__(self, meat, onion, carrot):
        self.meat = meat
        self.onion = onion
        self.__carrot = carrot
        
    def __str__(self):
        return f"Ang lumpia ko ay may {self.meat}, {self.onion}, {self.__carrot}"
    def may_carrots_ba(self, bata):
        if not bata:
            return self.__carrot
        else:
            return self.__carrot
            
            
lumpiang_shanghai = Lumpia_wrapper("baboy", "isang sibuyas", "isang carrot")
print(lumpiang_shanghai.may_carrots_ba(False))
# (__) private is accessible 
# (_) protected is still accessible