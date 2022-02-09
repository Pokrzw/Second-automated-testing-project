from unittest.mock import Mock, patch
import unittest
from src.app import App
from src.database import Database
from src.schemas.notes import Note
from assertpy import assert_that

class TestAddNote(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()
    @patch("src.database.Database.add_note")
    def test_add_note_success(self, mock_add):
        mock_add.return_value = 1
        assert_that(self.app.add_note(1,1,1,1,"Lorem Ipsum")).is_equal_to(True)

    @patch("src.database.Database.add_note")
    def test_add_note_fail(self, mock_add):
        mock_add.return_value = -1
        assert_that(self.app.add_note(10, 10, 10, 10, "Lorem ipsum")).is_equal_to(False)

class TestEditNote(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()
    @patch("src.database.Database.check_if_note_exists")
    def test_edit_note_fail_doesnt_exist(self, mock_check):
        mock_check.return_value = None
        assert_that(self.app.edit_note(10,1,1,1,"Lorem")).is_equal_to("This note does not exist")

    @patch("src.database.Database.edit_note")
    @patch("src.database.Database.check_if_note_exists")
    def test_edit_note_fail(self, mock_check, mock_edit):
        mock_check.return_value = "note instance"
        mock_edit.return_value = -1
        assert_that(self.app.edit_note(1,1,1,1,"Lorem")).is_equal_to(False)

    @patch("src.database.Database.edit_note")
    @patch("src.database.Database.check_if_note_exists")
    def test_edit_note_success(self, mock_check, mock_edit):
        mock_check.return_value = "note instance"
        mock_edit.return_value = 1
        assert_that(self.app.edit_note(1,1,1,1,"lorem")).is_equal_to(True)

class TestDeleteNote(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()
    @patch("src.database.Database.check_if_note_exists")
    def test_delete_note_fail_doesnt_exist(self, mock_check):
        mock_check.return_value = None
        assert_that(self.app.delete_note(10)).is_equal_to("This note does not exist")

    @patch("src.database.Database.delete_note")
    @patch("src.database.Database.check_if_note_exists")
    def test_delete_note_fail(self, mock_check, mock_delete):
        mock_check.return_value = "note instance"
        mock_delete.return_value = -1
        assert_that(self.app.delete_note(1)).is_equal_to(False)

    @patch("src.database.Database.delete_note")
    @patch("src.database.Database.check_if_note_exists")
    def test_edit_note_fail(self, mock_check, mock_delete):
        mock_check.return_value = "note instance"
        mock_delete.return_value = 1
        assert_that(self.app.delete_note(1)).is_equal_to(True)