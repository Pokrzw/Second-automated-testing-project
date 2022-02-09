from unittest.mock import Mock, patch
import unittest
from src.app import App
from src.database import Database
from src.schemas.grades import Grade
from assertpy import assert_that

class TestAddGrade(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()
    @patch("src.database.Database.add_grade")
    def test_add_grade_success(self, mock_add):
        mock_add.return_value = 1
        assert_that(self.app.add_grade(1,1,1,1,4)).is_equal_to(True)

    @patch("src.database.Database.add_grade")
    def test_add_grade_fail(self, mock_add):
        mock_add.return_value = -1
        assert_that(self.app.add_grade(10, 10, 10, 10, 4)).is_equal_to(False)

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