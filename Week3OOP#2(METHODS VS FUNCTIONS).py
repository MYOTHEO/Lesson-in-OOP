class character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def describe(self, course):
        print(f"Si {self.name} ay {self.age} taong gulang na sa {course}.")
        
student = character('Meynard', 19)
student.describe("BSIT")
'''
student = character('Corbet', 19)
student.describe("MASCOM")
'''