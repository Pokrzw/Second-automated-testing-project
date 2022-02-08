import unittest
import re
from src.schemas.student import Student
from unittest.mock import Mock, patch
import nose2
import assertpy
from assertpy import assert_that


class TestCreateUczen(unittest.TestCase):
    @patch("src.database.Database.createStudent")
    def test_create_uczen_incorrect_name(self, mock_create_student):
        mock_create_student.name = "343fdsd"
        assert_that(Student.checkName).raises(ValueError).when_called_with(mock_create_student.name)

    def test_create_uczen_wrong_classcode(self):
        mock_Input_data = Mock(classCode='aa')
        assert_that(Student.checkClassCode).raises(ValueError).when_called_with(mock_Input_data.classCode)

    @patch("src.database.Database.createStudent")
    def test_create_uczen_correct_input(self, mock_create):
        mock_create.name = "Jan"
        mock_create.surname = "Kowalski"
        mock_create.classCode = "3A"
        newStudent = Student(mock_create.name, mock_create.surname, mock_create.classCode)
        assert_that(newStudent).is_instance_of(Student)
