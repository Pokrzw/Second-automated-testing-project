import unittest
import re
from src.database import Database
from src.schemas.teacher import Teacher
from unittest.mock import Mock, patch, create_autospec
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

class TestAppEditTeacher(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()

    @patch('src.database.Database.check_if_teacher_exists')
    def test_edit_student_fail_techer_doesnt_exist(self, mock_search):
        mock_search.return_value = False
        assert_that(self.app.edit_teacher(1,"","")).is_equal_to("Teacher does not exists")

    @patch('src.database.Database.edit_teacher')
    @patch('src.database.Database.check_if_teacher_exists')
    def test_edit_student_success(self, mock_search, mock_edit_teacher):
        mock_search.return_value = {"id":1, "name": "Jan", "surname":"Kowalski"}
        mock_edit_teacher.return_value = 1
        assert_that(self.app.edit_teacher(1,"","")).is_equal_to(True)

class TestAppDeleteTeacher(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()

    @patch('src.database.Database.check_if_teacher_exists')
    def test_delete_teacher_fail_no_id(self, mock_search):
        mock_search.return_value = False
        assert_that(self.app.delete_teacher(1)).is_equal_to("Teacher does not exists")

    @patch('src.database.Database.check_if_teacher_exists')
    @patch('src.database.Database.delete_teacher')
    def test_delete_teacher_success(self, mock_delete, mock_search):
        mock_search.return_value = "Student object"
        mock_delete.return_value = 1
        assert_that(self.app.delete_teacher(1)).is_equal_to(True)

    @patch('src.database.Database.check_if_teacher_exists')
    @patch('src.database.Database.delete_teacher')
    def test_delete_teacher_fail(self, mock_delete, mock_search):
        mock_search.return_value = "Teacher object"
        mock_delete.return_value = -1
        assert_that(self.app.delete_teacher(1)).is_equal_to(False)

class TestGetGradesGivenByTeacher(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()

    @patch('src.database.Database.check_if_teacher_exists')
    def test_grades_given_by_teacher_fail_no_id(self, mock_search):
        mock_search.return_value = None
        assert_that(self.app.get_grades_given_by_teacher(1)).is_equal_to("This teacher does not exist")

    @patch('src.database.Database.getAllGrades')
    @patch('src.database.Database.check_if_teacher_exists')
    def test_grades_given_by_teacher_success(self, mock_search, mock_all_grades):
        mock_grade1 = Mock(teacher_id=1, value=5)
        mock_grade2 = Mock(teacher_id=4, value=3)
        mock_grade3 = Mock(teacher_id=1, value=4)
        mock_all_grades.return_value = [mock_grade1, mock_grade2, mock_grade3]
        mock_search.return_value = 1
        assert_that(self.app.get_grades_given_by_teacher(1)).is_equal_to([mock_grade1, mock_grade3])

class TestGetSubjectsByTeacher(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()

    @patch('src.database.Database.check_if_teacher_exists')
    def test_grades_given_by_teacher_fail_no_id(self, mock_search):
        mock_search.return_value = None
        assert_that(self.app.get_subjects_taught_by_teacher(1)).is_equal_to("This teacher does not exist")

    @patch('src.database.Database.get_teacher_instance')
    @patch('src.database.Database.check_if_teacher_exists')
    def test_grades_given_by_teacher_success(self, mock_search, mock_teacher_instance):
        mock_teacher = create_autospec(Teacher)
        mock_teacher.taught_subjects=["Przyroda","Matematyka"]
        mock_search.return_value = mock_teacher
        mock_teacher_instance.return_value = mock_teacher
        assert_that(self.app.get_subjects_taught_by_teacher(1)).is_equal_to(["Przyroda","Matematyka"])
