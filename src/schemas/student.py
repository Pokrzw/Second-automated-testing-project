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
        namePattern = '[A-Z][a-z]*'
        if namePattern.match(name)!=None:
            return 
    def checkClassCode(self, classCode):
        pass