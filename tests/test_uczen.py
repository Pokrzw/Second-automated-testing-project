import unittest
import re

import src.database
from src.schemas.student import Student
from unittest.mock import Mock, patch
import nose2
import assertpy
from assertpy import assert_that
from src.app import App


class TestCreateUczen(unittest.TestCase):
    @patch("src.database.Database.add_student")
    def test_create_uczen_incorrect_name(self, mock_create_student):
        mock_create_student.name = "343fdsd"
        assert_that(Student.checkName).raises(ValueError).when_called_with(mock_create_student.name)

    def test_create_uczen_wrong_classcode(self):
        mock_Input_data = Mock(classCode='aa')
        assert_that(Student.checkClassCode).raises(ValueError).when_called_with(mock_Input_data.classCode)

    @patch("src.database.Database.add_student")
    def test_create_uczen_correct_input(self, mock_create):
        mock_create.name = "Jan"
        mock_create.surname = "Kowalski"
        mock_create.classCode = "3A"
        newStudent = Student(mock_create.name, mock_create.surname, mock_create.classCode)
        assert_that(newStudent).is_instance_of(Student)


class TestAppCreateStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_results = Mock(side_effect=[1,-1])

    @patch("src.database.Database.add_student")
    def test_create_student_ok(self,mock_adding_student):
        mock_adding_student.return_value = self.mock_results()
        print(mock_adding_student.return_value)
        assert_that(App.create_student("Jan", "Kowalski", "3C")).is_equal_to(1)

    @patch("src.database.Database.add_student")
    def test_create_student_fail(self, mock_adding_student):
        self.mock_results()
        mock_adding_student.return_value = self.mock_results()
        assert_that(App.create_student("Jan", "9879", "xx")).is_equal_to(-1)

class TestAppEditUczen(unittest.TestCase):
    @patch('src.database.Database.search_student_by_id')
    def test_edit_student_fail(self, mock_search):
        mock_search.return_value = None
        assert_that(App.edit_student).raises(ValueError).when_called_with(5,'name','dur','3c')

    @patch('src.database.Database.edit_student')
    @patch('src.database.Database.search_student_by_id')
    def test_edit_student_fail(self, mock_search, mock_edit_student):
        mock_search.return_value = {"id":1, "name": "Jan", "surname":"Kowalski", "classCode":"5D"}
        mock_edit_student.return_value = {"id":1, "name": "Jan", "surname":"Kowalski", "classCode":"5A"}
        assert_that(App.edit_student(1,"","","5A")).is_equal_to({"id":1, "name": "Jan", "surname":"Kowalski", "classCode":"5A"})
