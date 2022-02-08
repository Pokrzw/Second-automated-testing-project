import re


class Student:
    id = 0

    def __init__(self, name: str, surname: str, classCode: str):
        self.id = Student.id
        self.name = self.checkName(name)
        self.surname = self.checkName(surname)
        self.classCode = self.checkClassCode(classCode)
        self._grades = []
        self._notes = []
        Student.id += 1

    @staticmethod
    def checkName(name):
        namePattern = r'[A-Z][a-z]*'
        if re.fullmatch(namePattern, name) is not None:
            return name
        raise ValueError("Given name is not correct")

    @staticmethod
    def checkClassCode(classCode):
        classCodePattern = r'[1-8][A-G]'
        if re.fullmatch(classCodePattern, classCode) is not None:
            return classCode
        raise ValueError("Given classCode is not correct")

    @property
    def grades(self):
        return self._grades

    @property
    def notes(self):
        return self._notes

