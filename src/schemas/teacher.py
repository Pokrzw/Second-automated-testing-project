import re
class Teacher:
    id= 0
    def __init__(self, name: str, surname: str):
        self.id = Teacher.id
        self.name = self.checkName(name)
        self.surname = self.checkName(surname)
        self._taught_classess = []
        self._taught_subjects = []
        Teacher.id += 1

    @staticmethod
    def checkName(name):
        namePattern = r'[A-Z][a-z]*'
        if re.fullmatch(namePattern, name) is not None:
            return name
        raise ValueError("Given name is not correct")

    @property
    def taught_classess(self):
        return self._taught_classess

    @property
    def taught_subjects(self):
        return self._taught_subjects

