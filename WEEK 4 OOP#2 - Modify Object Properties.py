class Course:
    def __init__(self, name):
        self.name = name
it = Course("Information Technology")
cs = Course("Computer Science")
print(cs.name)
print(it.name)
it.name = "BSIT" #updated ver
print(it.name)
print(cs.name)
