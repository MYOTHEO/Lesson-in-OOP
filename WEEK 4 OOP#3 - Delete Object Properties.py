class Pagkain:
    def __init__(self, name):
        self.name = name
burger = Pagkain("Angels")
del burger.name #deleted, will make an error if run
print(burger.name)

'''
IF YOU WANT TO GET THE VALUE OF DELETED ONE:
class Pagkain:
    def __init__(self, name):
        self.name = name
burger = Pagkain("Angels")
del burger.name #deleted, will make an error if run
bruger.name = ""  <------    #add this line of code to print the output of the deleted value
print(burger.name)
'''