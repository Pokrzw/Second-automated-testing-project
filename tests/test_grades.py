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