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
        mock_Input_data = Mock(classCode = 'aa')
        assert_that(Student.checkClassCode).raises(ValueError).when_called_with(mock_Input_data.classCode)
