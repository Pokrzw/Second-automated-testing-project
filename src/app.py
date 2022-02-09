from src.database import Database
from src.schemas.student import Student
class App:
    def connect_to_database(self,database,paswd):
        if paswd == database.password:
            return f"Connected to {database.database_name} on port {database.port}"
        return "Couldn't connect to database - wrong password"

    @staticmethod
    def create_student(name, surname, classCode):
        Database.add_student(name, surname, classCode)
        if Database.add_student_response():
            return "Dodano ucznia"
        return "Nie dodano ucznia"

    @staticmethod
    def edit_student(id, name, surname, classCode):
        if Database.search_student_by_id(id) is None:
            raise ValueError("Nie ma studenta o podanym id")
        Database.edit_student(id, name, surname, classCode)
        return Database.edit_student_response()

    @staticmethod
    def delete_student(id):
        if Database.search_student_by_id(id) is None:
            raise ValueError("Nie ma studenta o podanym id")
        else:
            Database.delete_student(id)
            return Database.delete_student_response()

    @staticmethod
    def add_subject(name, teacher):
        if Database.check_if_subject_exists(name) is True:
            return "Subject already exists"
        Database.create_subject(name, teacher)
        return Database.create_subject_response()

