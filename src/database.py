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

    def create_przedmiot(self):
        pass
