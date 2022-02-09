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

    @staticmethod
    def edit_subject(name, teacher):
        if Database.check_if_subject_exists(name) is False:
            return "Subject does not exists"
        Database.edit_subject(name, teacher)
        return Database.edit_subject_response()

    @staticmethod
    def delete_subject(name):
        if Database.check_if_subject_exists(name) is False:
            return "Subject does not exists"
        Database.delete_subject(name)
        return Database.delete_subject_response()

    @staticmethod
    def add_teacher(name, surname):
        Database.add_teacher(name, surname)
        return Database.add_teacher_response()

    @staticmethod
    def edit_teacher(id,name, surname):
        if Database.check_if_teacher_exists(id) is False:
            return "Teacher does not exists"
        Database.edit_teacher(id,name, surname)
        return Database.edit_teacher_response()

    @staticmethod
    def delete_teacher(id):
        if Database.check_if_teacher_exists(id) is False:
            return "Teacher does not exists"
        Database.delete_teacher(id)
        return Database.delete_teacher_response()

    @staticmethod
    def add_grade(grade_id, student_id, teacher_id, subject_id, value):
        Database.add_grade(grade_id, student_id, teacher_id, subject_id, value)
        return