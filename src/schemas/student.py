import re
class Student:
    id = 0
    def __init__(self, name:str, surname:str, classCode:str, grades:list, notes:list ):
        self.name = name
        self.surname = surname
        self.classCode = classCode
        self.grades = []
        self.notes = []
    def checkName(self, name):
        pattern = re.compile('[A-Z]{1}[a-z]')
        pattern.match(string)

        nameRegex =
    def checkClassCode(self, classCode):
        pass