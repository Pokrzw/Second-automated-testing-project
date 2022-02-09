import unittest
import re
from src.database import Database
from src.schemas.subject import Subject
from unittest.mock import Mock, patch
import nose2
import assertpy
from assertpy import assert_that
from src.app import App


class TestCreateSubject(unittest.TestCase):
    def test_subject_init(self):
        assert_that(Subject("Przyroda", 'Jan Kowalski')).is_instance_of(Subject)

class Test_app_add_subject(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()

    @patch('src.database.Database.create_subject')
    @patch('src.database.Database.check_if_subject_exists')
    def test_add_subject_success(self, mock_check, mock_create):
        mock_check.return_value = False
        mock_create.return_value = 1
        assert_that(self.app.add_subject("Matematyka","Marcin Nowak")).is_equal_to(True)

    @patch('src.database.Database.check_if_subject_exists')
    def test_add_subject_fail_subject_exists(self, mock_check):
        mock_check.return_value = True
        assert_that(self.app.add_subject("Matematyka", "Marcin Nowak")).is_equal_to("Subject already exists")

    @patch('src.database.Database.create_subject')
    @patch('src.database.Database.check_if_subject_exists')
    def test_add_subject_fail(self, mock_check, mock_create):
        mock_check.return_value = False
        mock_create.return_value = -1
        assert_that(self.app.add_subject("Fizyka", "Marcin Nowak")).is_equal_to(False)

class Test_app_edit_subject(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()

    @patch('src.database.Database.edit_subject')
    @patch('src.database.Database.check_if_subject_exists')
    def test_edit_subject_success(self, mock_check, mock_edit):
        mock_check.return_value = True
        mock_edit.return_value = 1
        assert_that(self.app.edit_subject("Matematyka","Marcin Nowak")).is_equal_to(True)

    @patch('src.database.Database.check_if_subject_exists')
    def test_edit_subject_fail_subject_doesnt_exist(self, mock_check):
        mock_check.return_value = False
        assert_that(self.app.edit_subject("Matematyka", "Marcin Nowak")).is_equal_to("Subject does not exists")

    @patch('src.database.Database.edit_subject')
    @patch('src.database.Database.check_if_subject_exists')
    def test_add_subject_fail(self, mock_check, mock_edit):
        mock_check.return_value = True
        mock_edit.return_value = -1
        assert_that(self.app.edit_subject("Fizyka", "Marcin Nowak")).is_equal_to(False)

class Test_app_delete_subject(unittest.TestCase):
    def setUp(self) -> None:
        self.app = App()

    @patch('src.database.Database.delete_subject')
    @patch('src.database.Database.check_if_subject_exists')
    def test_delete_subject_success(self, mock_check, mock_delete):
        mock_check.return_value = True
        mock_delete.return_value = 1
        assert_that(self.app.delete_subject("Matematyka")).is_equal_to(True)

    @patch('src.database.Database.check_if_subject_exists')
    def test_edit_subject_fail_subject_doesnt_exist(self, mock_check):
        mock_check.return_value = False
        assert_that(self.app.delete_subject("Matematyka")).is_equal_to("Subject does not exists")

    @patch('src.database.Database.delete_subject')
    @patch('src.database.Database.check_if_subject_exists')
    def test_add_subject_fail(self, mock_check, mock_delete):
        mock_check.return_value = True
        mock_delete.return_value = -1
        assert_that(self.app.delete_subject("Fizyka")).is_equal_to(False)
