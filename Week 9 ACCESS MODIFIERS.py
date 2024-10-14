#Encapsulation
class Lumpia_wrapper:
    def __init__(self, meat, onion, carrot):
        self.meat = meat
        self.onion = onion
        self._carrot = carrot
        
        def __str__(self):
            return f"Ang lumpia ko ay may {self.meat}, {self.onion}, {self._carrot}"

lumpiang_shanghai = Lumpia_wrapper("baboy", "isang sibuyas", "isang carrot")
print(lumpiang_shanghai._carrot)
# (__) private is accessible 
# (_) protected is still accessible