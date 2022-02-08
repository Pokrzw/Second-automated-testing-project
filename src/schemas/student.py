class Student:
    id = 0
    def __init__(self, name:str, surname:str, classCode:str, grades:list, notes:list ):
        self.name = name
        self.surname = surname
        self.classCode = classCode
        self.grades = []
        self.notes = []
    