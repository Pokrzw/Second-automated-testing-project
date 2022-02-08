import re
class Student:
    id = 0
    def __init__(self, name:str, surname:str, classCode:str, grades:list, notes:list ):
        self.id = Student.id
        self.name = name.checkName(name)
        self.surname = surname
        self.classCode = classCode
        self.grades = []
        self.notes = []
        id += 1
    def checkName(self, name):
        namePattern = '[A-Z][a-z]*'
        if namePattern.match(name) is not None:
            return name
        raise ValueError("Given name is not correct")

    def checkClassCode(self, classCode):
        classCodePattern = '[1-8][A-G]'
        if classCodePattern.match(classCode) is not None:
            return classCode
        raise ValueError("Given classCode is not correct")

