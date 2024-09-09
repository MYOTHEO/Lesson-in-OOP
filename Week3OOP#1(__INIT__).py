class character:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
student = character('Meynard', 19)
student2 = character('Sean', 20)
print(student.name, student.age, student2.name, student2.age)