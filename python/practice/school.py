class Student:
    def __init__(self, name, age, gpa, major):
        self.name = name
        self.age = age
        self.gpa = gpa
        self.major = major
    
    def graduateGPA(self):
        if self.gpa >= 5:
            return True
        else:
            return False