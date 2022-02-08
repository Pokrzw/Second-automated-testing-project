from src.database import Database
class FakeDatabase(Database):
    def getAllStudents(self):
        pass
    def getStudentGrades(self, student_id):
        pass
    def getStudentNotes(self, student_id):
        pass
    def createStudent(self,name:str, surname:str, classCode:str):
        pass
    def deleteStudent(self, student_id):
        pass