class Database:
    def __init__(self, database_name:str, password:str, port:int):
        pass
    def add_student(self):
        pass
    @staticmethod
    def add_student_response():
        if Database.add_student()==-1:
            return False
        return True
    def edit_student(self, student_id, name, surname, classCode):
        pass
    @staticmethod
    def edit_student_response():
        if Database.edit_student() == -1:
            return False
        return True
    def search_student_by_id(self, student_id):
        pass
    def delete_student(self, student_id):
        pass

    @staticmethod
    def delete_student_response():
        if Database.delete_student() == -1:
            return False
        return True

    def create_subject(self):
        pass

    def check_if_subject_exists(self, subject):
        pass

    @staticmethod
    def create_subject_response():
        if Database.create_subject()==-1:
            return False
        return True

    def edit_subject(self):
        pass

    @staticmethod
    def edit_subject_response():
        if Database.edit_subject() == -1:
            return False
        return True

    def delete_subject(self):
        pass

    @staticmethod
    def delete_subject_response():
        if Database.delete_subject() == -1:
            return False
        return True

    def add_teacher(self, name, surname):
        pass

    @staticmethod
    def add_teacher_response():
        if Database.add_teacher() == -1:
            return False
        return True

    def check_if_teacher_exists(self):
        pass

    def edit_teacher(self):
        pass

    @staticmethod
    def edit_teacher_response():
        if Database.edit_teacher() == -1:
            return False
        return True

    def delete_teacher(self):
        pass

    @staticmethod
    def delete_teacher_response():
        if Database.delete_teacher() == -1:
            return False
        return True

    def add_grade(self):
        pass

    @staticmethod
    def add_grade_response():
        if Database.add_grade() == -1:
            return False
        return True

    @staticmethod
    def check_if_grade_exists(id):
        pass

    def edit_grade(self):
        pass

    @staticmethod
    def edit_grade_response():
        if Database.edit_grade() == -1:
            return False
        return True
