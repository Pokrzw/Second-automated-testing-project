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
        name = "Przyroda"
        nauczyciel = 'Jan Kowalski'
        assert_that(Subject(name, nauczyciel)).is_instance_of(Subject)


