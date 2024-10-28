#Encapsulation Getter
class Lumpia_wrapper:
    def __init__(self, meat, onion, carrot):
        self.meat = meat            #public
        self._onion = onion          #protected
        self.__carrot = carrot      #private
        
    def __str__(self):
        return f"Ang lumpia ko ay may {self.meat}, {self._onion}, {self.__carrot}"
    def may_carrots_ba(self): #getter method
            return self.__carrot
    def set_carrot(self, bagong_value): #setter method
        self.__carrot = bagong_value
            
lumpiang_shanghai = Lumpia_wrapper("baboy", "isang sibuyas", "isang carrot")
lumpiang_shanghai.set_carrot = ("limang carrot")
lumpiang_shanghai.__carrot = "dalawang carrot"
print(lumpiang_shanghai.__carrot)
print(lumpiang_shanghai.set_carrot)
# (__) private is accessible 
# (_) protected is still accessible
