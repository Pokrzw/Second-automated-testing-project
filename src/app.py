from src.database import Database
from src.schemas.student import Student
class App:
    @staticmethod
    def create_student(name, surname, classCode):
        Database.add_student(name, surname, classCode)
        if Database.add_student(name, surname, classCode) == -1:
            return -1
        return 1

    @staticmethod
    def edit_student(id, name, surname, classCode):
        if Database.search_student_by_id(id) is None:
            raise ValueError("Nie ma studenta o podanym id")
        edited_student = Database.search_student_by_id(id)
        Database.edit_student(id, name, surname, classCode)
        return Database.edit_student(id, name, surname, classCode)

    @staticmethod
    def delete_student(id):
        if Database.search_student_by_id(id) is None:
            raise ValueError("Nie ma studenta o podanym id")
        else:
            deleted_student = Database.search_student_by_id(id)
            Database.delete_student(id)
