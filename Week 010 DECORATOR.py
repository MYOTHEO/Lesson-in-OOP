#Decorator
class Bday:
    def __init__(self, name):
        self.name = name
    def handaan(self, func_name):
        def pinyata(*args, **kwargs):
            print("Cake, Lechon, Spag...")
            func_name(*args, **kwargs)
            print("Success!!!")
        return pinyata
shanghai = Bday ("Shanghai")

@shanghai.handaan
def eatAllYouCan(mga_pagkain):
    print(mga_pagkain)
eatAllYouCan("Pritong Manok")


'''
class Regalo:
    def __init__(self, laman, wrapper):
        self.laman = laman
        self.wrapper = wrapper
    def buksan(self, func):
        def wrapper_mthd(*args, **kwargs):
            print("Openning regalo...")
            func(*args, **kwargs)
            print("Closing regalo..")
        return wrapper_mthd
regalo_ko = Regalo ("Choco", "Red")

@regalo_ko.buksan
def para_kanino(receiver):
    print(f"Ito ay para kay {receiver}")
para_kanino("Nanay")