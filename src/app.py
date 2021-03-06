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
        return Database.add_grade_response()

    @staticmethod
    def edit_grade(grade_id, student_id, teacher_id, subject_id, value):
        if Database.check_if_grade_exists(grade_id) is None:
            return "This grade does not exist"
        Database.edit_grade(grade_id, student_id, teacher_id, subject_id, value)
        return Database.edit_grade_response()

    @staticmethod
    def delete_grade(grade_id):
        if Database.check_if_grade_exists(grade_id) is None:
            return "This grade does not exist"
        Database.delete_grade(grade_id)
        return Database.delete_grade_response()

    @staticmethod
    def add_note(note_id, student_id, teacher_id, subject_id, text):
        Database.add_note()
        return Database.add_note_response()

    @staticmethod
    def edit_note(note_id, student_id, teacher_id, subject_id, text):
        if Database.check_if_note_exists(note_id) is None:
            return "This note does not exist"
        Database.edit_note(note_id, student_id, teacher_id, subject_id, text)
        return Database.edit_note_response()

    @staticmethod
    def delete_note(note_id):
        if Database.check_if_note_exists(note_id) is None:
            return "This note does not exist"
        Database.delete_note(note_id)
        return Database.delete_note_response()

    @staticmethod
    def show_student_grades(student_id):
        if Database.search_student_by_id() is None:
            return "This student does not exist"
        student = Database.get_student_instance(student_id)
        return student.grades

    @staticmethod
    def show_student_notes(student_id):
        if Database.search_student_by_id() is None:
            return "This student does not exist"
        student = Database.get_student_instance(student_id)
        return student.notes

    @staticmethod
    def get_grades_given_by_teacher(teacher_id):
        if Database.check_if_teacher_exists(teacher_id) is None:
            return "This teacher does not exist"
        resultsArray = []
        for grade in Database.getAllGrades():
            if grade.teacher_id == teacher_id:
                resultsArray.append(grade)
        return resultsArray

    @staticmethod
    def get_subjects_taught_by_teacher(teacher_id):
        if Database.check_if_teacher_exists(teacher_id) is None:
            return "This teacher does not exist"
        teacher = Database.get_teacher_instance(teacher_id)
        return teacher.taught_subjects

    @staticmethod
    def get_avg_grade_of_class(class_code, subject_id):
        gradeArray = Database.getAllGrades()
        gradeSum = 0
        gradeNumber = 0
        for grade in gradeArray:
            if grade.subject_id == subject_id:
                student = Database.get_student_instance(grade.student_id)
                if student.classCode == class_code:
                    gradeSum += grade.value
                    gradeNumber += 1
        return gradeSum/gradeNumber