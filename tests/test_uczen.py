import unittest
import re
from src.database import Database
from src.schemas.student import Student
from unittest.mock import Mock, patch
import nose2
import assertpy
from assertpy import assert_that
from src.app import App


class TestCreateStudent(unittest.TestCase):
    def test_create_student_incorrect_name(self):
        name = "343fdsd"
        assert_that(Student.checkName).raises(ValueError).when_called_with(name)

    def test_create_student_wrong_classcode(self):
        classCode='aa'
        assert_that(Student.checkClassCode).raises(ValueError).when_called_with(classCode)

    def test_create_student_correct_input(self):
        name = "Jan"
        surname = "Kowalski"
        classCode = "3A"
        newStudent = Student(name, surname, classCode)
        assert_that(newStudent).is_instance_of(Student)

class TestAppConnectToDataabse(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()
        self.database = Database("mongo",'pwd',4000)

    @patch("src.database.Database")
    def test_connect_to_database_fail(self, mock_database):
        mock_database.database_name = "mongo"
        mock_database.password = "pwd"
        mock_database.port = 4000
        assert_that(self.app.connect_to_database(mock_database, "1234")).is_equal_to("Couldn't connect to database - wrong password")

    @patch("src.database.Database")
    def test_connect_to_database_success(self, mock_database):
        mock_database.database_name = "mongo"
        mock_database.password = "pwd"
        mock_database.port = 4000
        assert_that(self.app.connect_to_database(mock_database, "pwd")).is_equal_to(
            "Connected to mongo on port 4000")


class TestAppCreateStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_results = Mock(side_effect=[1,-1])
        self.app = App()

    @patch("src.database.Database.add_student")
    def test_create_student_ok(self,mock_adding_student):
        mock_adding_student.return_value = self.mock_results()
        assert_that(self.app.create_student("Jan", "Kowalski", "3C")).is_equal_to("Dodano ucznia")

    @patch("src.database.Database.add_student")
    def test_create_student_fail(self, mock_adding_student):
        self.mock_results()
        mock_adding_student.return_value = self.mock_results()
        assert_that(self.app.create_student("Jan", "9879", "xx")).is_equal_to("Nie dodano ucznia")

class TestAppEditStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()

    @patch('src.database.Database.search_student_by_id')
    def test_edit_student_fail(self, mock_search):
        mock_search.return_value = None
        assert_that(self.app.edit_student).raises(ValueError).when_called_with(5,'name','dur','3c')

    @patch('src.database.Database.edit_student')
    @patch('src.database.Database.search_student_by_id')
    def test_edit_student_success(self, mock_search, mock_edit_student):
        mock_search.return_value = {"id":1, "name": "Jan", "surname":"Kowalski", "classCode":"5D"}
        mock_edit_student.return_value = 1
        assert_that(self.app.edit_student(1,"","","5A")).is_equal_to(True)

class TestAppDeleteStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()
    @patch('src.database.Database.search_student_by_id')
    def test_delete_student_fail_no_id(self, mock_search):
        mock_search.return_value = None
        assert_that(self.app.delete_student).raises(ValueError).when_called_with("g")


    @patch('src.database.Database.search_student_by_id')
    @patch('src.database.Database.delete_student')
    def test_delete_student_fail(self, mock_delete, mock_search):
        mock_search.return_value = "Student object"
        mock_delete.return_value = -1
        assert_that(self.app.delete_student(1)).is_equal_to(False)
