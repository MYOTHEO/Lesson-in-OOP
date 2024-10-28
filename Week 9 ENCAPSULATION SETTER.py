#Encapsulation
class Lumpia_wrapper:
    def __init__(self, meat, onion, carrot):
        self.__meat = meat
        self.onion = onion
        self.carrot = carrot
        
        def __str__(self):
            return f"Ang lumpia ko ay may {self.__meat}, {self.onion}, {self.carrot}"

lumpiang_shanghai = Lumpia_wrapper("baboy", "isang sibuyas", "isang carrot")
print(lumpiang_shanghai.__meat)
