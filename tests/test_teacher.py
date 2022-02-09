import unittest
import re
from src.database import Database
from src.schemas.teacher import Teacher
from unittest.mock import Mock, patch
import nose2
import assertpy
from assertpy import assert_that
from src.app import App


class TestCreateTeacher(unittest.TestCase):
    def test_create_teacher_incorrect_name(self):
        name = "343fdsd"
        assert_that(Teacher.checkName).raises(ValueError).when_called_with(name)

    def test_create_teacher_correct_input(self):
        name = "Jan"
        surname = "Kowalski"
        newTeacher = Teacher(name, surname)
        assert_that(newTeacher).is_instance_of(Teacher)

class TestAppCreateTeacher(unittest.TestCase):
    def setUp(self) -> None:
        self.mock_results = Mock(side_effect=[1,-1])
        self.app = App()

    @patch("src.database.Database.add_teacher")
    def test_create_teacher_ok(self,mock_adding_teacher):
        mock_adding_teacher.return_value = self.mock_results()
        assert_that(self.app.add_teacher("Jan", "Kowalski")).is_equal_to(True)

    @patch("src.database.Database.add_teacher")
    def test_create_teacher_fail(self, mock_adding_teacher):
        self.mock_results()
        mock_adding_teacher.return_value = self.mock_results()
        assert_that(self.app.add_teacher("Jan", "Kowalski")).is_equal_to(False)

# class TestAppEditStudent(unittest.TestCase):
#     def setUp(self) -> None:
#         self.app = App()
#
#     @patch('src.database.Database.search_student_by_id')
#     def test_edit_student_fail(self, mock_search):
#         mock_search.return_value = None
#         assert_that(self.app.edit_student).raises(ValueError).when_called_with(5,'name','dur','3c')
#
#     @patch('src.database.Database.edit_student')
#     @patch('src.database.Database.search_student_by_id')
#     def test_edit_student_success(self, mock_search, mock_edit_student):
#         mock_search.return_value = {"id":1, "name": "Jan", "surname":"Kowalski", "classCode":"5D"}
#         mock_edit_student.return_value = 1
#         assert_that(self.app.edit_student(1,"","","5A")).is_equal_to(True)
#
# class TestAppDeleteStudent(unittest.TestCase):
#     def setUp(self) -> None:
#         self.app = App()
#     @patch('src.database.Database.search_student_by_id')
#     def test_delete_student_fail_no_id(self, mock_search):
#         mock_search.return_value = None
#         assert_that(self.app.delete_student).raises(ValueError).when_called_with("g")
#
#
#     @patch('src.database.Database.search_student_by_id')
#     @patch('src.database.Database.delete_student')
#     def test_delete_student_fail(self, mock_delete, mock_search):
#         mock_search.return_value = "Student object"
#         mock_delete.return_value = -1
#         assert_that(self.app.delete_student(1)).is_equal_to(False)
#
#     @patch('src.database.Database.search_student_by_id')
#     @patch('src.database.Database.delete_student')
#     def test_delete_student_success(self, mock_delete, mock_search):
#         mock_search.return_value = "Student object"
#         mock_delete.return_value = 1
#         assert_that(self.app.delete_student(1)).is_equal_to(True)