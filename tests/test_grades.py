from unittest.mock import Mock, patch
import unittest
from src.app import App
from src.database import Database
from src.schemas.grades import Grade
from assertpy import assert_that

class TestAddGrade(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()
    def test_grade_init(self):
        assert_that(Grade(1,2,3,4,5)).is_instance_of(Grade)
    @patch("src.database.Database.add_grade")
    def test_add_grade_success(self, mock_add):
        mock_add.return_value = 1
        assert_that(self.app.add_grade(1,1,1,1,4)).is_true()

    @patch("src.database.Database.add_grade")
    def test_add_grade_fail(self, mock_add):
        mock_add.return_value = -1
        assert_that(self.app.add_grade(10, 10, 10, 10, 4)).is_false()

class TestEditGrade(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()
    @patch("src.database.Database.check_if_grade_exists")
    def test_edit_grade_fail_doesnt_exist(self, mock_check):
        mock_check.return_value = None
        assert_that(self.app.edit_grade(10,1,1,1,3)).is_equal_to("This grade does not exist")

    @patch("src.database.Database.edit_grade")
    @patch("src.database.Database.check_if_grade_exists")
    def test_edit_grade_fail(self, mock_check, mock_edit):
        mock_check.return_value = "grade instance"
        mock_edit.return_value = -1
        assert_that(self.app.edit_grade(1,1,1,1,3)).is_equal_to(False)

    @patch("src.database.Database.edit_grade")
    @patch("src.database.Database.check_if_grade_exists")
    def test_edit_grade_fail(self, mock_check, mock_edit):
        mock_check.return_value = "grade instance"
        mock_edit.return_value = 1
        assert_that(self.app.edit_grade(1,1,1,1,3)).is_equal_to(True)

class TestDeleteGrade(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()
    @patch("src.database.Database.check_if_grade_exists")
    def test_delete_grade_fail_doesnt_exist(self, mock_check):
        mock_check.return_value = None
        assert_that(self.app.delete_grade(10)).is_equal_to("This grade does not exist")

    @patch("src.database.Database.delete_grade")
    @patch("src.database.Database.check_if_grade_exists")
    def test_edit_grade_fail(self, mock_check, mock_delete):
        mock_check.return_value = "grade instance"
        mock_delete.return_value = -1
        assert_that(self.app.delete_grade(1)).is_equal_to(False)

    @patch("src.database.Database.delete_grade")
    @patch("src.database.Database.check_if_grade_exists")
    def test_edit_grade_fail(self, mock_check, mock_delete):
        mock_check.return_value = "grade instance"
        mock_delete.return_value = 1
        assert_that(self.app.delete_grade(1)).is_equal_to(True)

class TestGetAvgGrade(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()

    @patch('src.database.Database.get_student_instance')
    @patch('src.database.Database.getAllGrades')
    def test_get_avg_grade_success(self, mock_get_all_grades, mock_student_instance):
        mock_grade1 = Mock(subject_id = 1, student_id = 3, value = 3)
        mock_grade2 = Mock(subject_id=1, student_id=2, value=3)
        mock_grade3 = Mock(subject_id=3, student_id=7, value=5)
        mock_grade4 = Mock(subject_id=1, student_id=4, value=3)
        mock_get_all_grades.return_value = [mock_grade1,mock_grade2,mock_grade3,mock_grade4]

        mock_st1 = Mock(student_id = 3, classCode = "5B")
        mock_st2 = Mock(student_id=2, classCode="5B")
        mock_st3 = Mock(student_id=7, classCode="5B")
        mock_st4 = Mock(student_id=4, classCode="2A")
        mock_student_instance.side_effect = [mock_st1,mock_st2,mock_st3,mock_st4]

        assert_that(self.app.get_avg_grade_of_class("5B",1)).is_equal_to(3.0)