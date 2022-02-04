# import unittest
# from unittest.mock import Mock, patch, mock_open
# from src.przedmiot import Przedmiot
# from nose2.tools import params
# from src.main import get_data, parse_przedmiot_data_from_csv, parse_uczen_data_from_csv
# from src.przedmiot import Przedmiot
# from assertpy import assert_that
# from src.errors import EmptyNameField, EmptyTeacherField
# from src.uczen import Uczen
# from mock_open import MockOpen
#
#
# def test_create_uczen():
#     mock_open = MockOpen()
#     mock_open["/path/to/file"].read_data = "Lorem;Ipsum;;"
#     mock_open["/path/to/bad_file"].side_effect = IOError()
#     with patch('__main__.open', mock_open):
#         parse_uczen_data_from_csv("/path/to/file")
#     assert_that(Uczen.get_wszyscy_uczniowie()).contains(['Lorem','Ipsum',[],[]])
#
#
#
#
