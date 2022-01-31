import unittest
from unittest.mock import Mock, patch
from nose2.tools import params
from main import get_data
from przedmiot import Przedmiot
from assertpy import assert_that
from errors import EmptyNameField, EmptyTeacherField, NotUniquePrzedmiot

@params((200, 'Dziala'),(400, -1))
def test_get_data( _status, _return):
    with patch('requests.get') as mock_get:
        mock_get.return_value.status_code = _status
        mock_get.return_value.json.return_value = _return
        assert get_data()==_return

class Test_przedmiot_class_INIT(unittest.TestCase):
    def setUp(self)-> None:
        Przedmiot.przedmiot_list=[]
        self.instance_1 = Przedmiot("Matematyka", "Jan Kowalski")
        self.instance_2 = Przedmiot("Polski", "Roman Nowak")
        Przedmiot.create_przedmiot("Astronomia","Sandzaja")
        Przedmiot.create_przedmiot("Szachy","Korwin")
        
    def test_przedmiot_init(self):
        self.assertEqual(self.instance_1.nazwa, "Matematyka")
    
    def test_check_if_przedmiot_unique_success_return(self):    
        self.assertEqual(self.instance_2._check_if_przedmiot_unique("Chemia"), "Chemia")
    
    def test_check_if_przedmiot_unique_success_przedmiot_list(self):
        self.instance_2._check_if_przedmiot_unique("Chemia")
        assert_that(self.instance_2.przedmiot_list).is_equal_to(['Matematyka', 'Polski', 'Astronomia', 'Szachy', 'Chemia'])
         
    def test_check_if_przedmiot_unique_epic_fail(self):
        with self.assertRaises(ValueError):
            self.instance_2._check_if_przedmiot_unique("Polski")  
        
    def tearDown(self):
        self.instance_1.nazwa = None
        self.instance_1.nauczyciel = None
        self.instance_2.nazwa = None
        self.instance_2.nauczyciel = None
        Przedmiot.przedmiot_list = []
        

class Test_przedmiot_class_CREATE(unittest.TestCase):
    pass
@params(('Chemia', 'Panda 3'),("Fizyka", 'Lorem Ipsum'), ("WDZ", "Jakis Koles"))
def test_create_przedmiot_success(_przedmiot, _nauczyciel):
    assert_that(Przedmiot.create_przedmiot(_przedmiot, _nauczyciel)).is_instance_of(Przedmiot)

@params(('prz1','', 'Panda 3',EmptyNameField),('prz2','Angielski', '',EmptyTeacherField),('prz3','', '',ValueError),("NieistniejacyPrzedmiot","NieistniejacyPrzedmiot", "Resnick", ValueError))
def test_create_przedmiot_failure(_placholder,_przedmiotErr, _nauczycielErr, _Err):
    instance = Przedmiot(_placholder, "Jan Kowalski")
    assert_that(Przedmiot.create_przedmiot).raises(_Err).when_called_with(_przedmiotErr, _nauczycielErr)


class Test_przedmiot_class_EDIT(unittest.TestCase):
    def setUp(self)-> None:
        Przedmiot.przedmiot_list=[]
        self.instance_1 = Przedmiot("Matematyka", "Jan Kowalski")
        self.instance_2 = Przedmiot("Polski", "Roman Nowak")
        Przedmiot.create_przedmiot("Astronomia","Sandzaja")
        Przedmiot.create_przedmiot("Szachy","Korwin")
        
    def test_edit_przedmiot_nauczyciel(self):
        Przedmiot.edit_przedmiot("Szachy","",'Panda 3')
        assert_that(Przedmiot.get_instance("Szachy").nauczyciel).is_equal_to("Panda 3")
    
    def test_edit_przedmiot_nazwa(self):
        Przedmiot.edit_przedmiot("Szachy","Nowa nazwa", '')
        assert_that(Przedmiot.get_przedmiots()).does_not_contain("Szachy, Korwin")  
        assert_that(Przedmiot.get_przedmiots()).contains("Nowa nazwa, Korwin")
    
    def test_edit_przedmiot_nazwa_and_nauczyciel(self):
        Przedmiot.edit_przedmiot("Szachy","Teraz", "Oba")
        assert_that(Przedmiot.get_przedmiots()).does_not_contain("Szachy, Korwin") 
        assert_that(Przedmiot.get_przedmiots()).contains("Teraz, Oba")

    def test_edit_przedmiot_failure_przedmiot_doesnt_exist(self):
        assert_that(Przedmiot.edit_przedmiot).raises(ValueError).when_called_with("Muzyka",'','')
    
    def test_edit_przedmiot_failure_przedmiot_already_exist(self):
        assert_that(Przedmiot.edit_przedmiot).raises(ValueError).when_called_with("Matematyka","Polski",'')
        
    def tearDown(self):
        self.instance_1.nazwa = None
        self.instance_1.nauczyciel = None
        self.instance_2.nazwa = None
        self.instance_2.nauczyciel = None
        Przedmiot.przedmiot_list = []
        
class Test_przedmiot_class_DELETE(unittest.TestCase):
    def setUp(self)-> None:
        Przedmiot.przedmiot_list=[]
        self.instance_1 = Przedmiot("Matematyka", "Jan Kowalski")
        self.instance_2 = Przedmiot("Polski", "Roman Nowak")
        Przedmiot.create_przedmiot("Astronomia","Sandzaja")
        Przedmiot.create_przedmiot("Szachy","Korwin")
        
    def test_delete_przedmiot_success(self):
        Przedmiot.delete_przedmiot("Szachy")
        assert_that(Przedmiot.edit_przedmiot).raises(ValueError).when_called_with("Szachy",'','')
    
    def test_delete_przedmiot_failure(self):
        assert_that(Przedmiot.delete_przedmiot).raises(ValueError).when_called_with("Kulturoznawstwo")
        
    def tearDown(self):
        self.instance_1.nazwa = None
        self.instance_1.nauczyciel = None
        self.instance_2.nazwa = None
        self.instance_2.nauczyciel = None
        Przedmiot.przedmiot_list = []

class Test_przedmiot_class_GET_PRZEDMIOTS(unittest.TestCase):
    def setUp(self)-> None:
        Przedmiot.przedmiot_list = []
        Przedmiot.instance_list = []
        Przedmiot.create_przedmiot("Matematyka", "Jan Kowalski")
        Przedmiot.create_przedmiot("Polski", "Roman Nowak")
        
    def test_get_przedmiots(self):
        assert_that(Przedmiot.get_przedmiots()).contains("Matematyka, Jan Kowalski","Polski, Roman Nowak")
        
    def tearDown(self):
        Przedmiot.delete_przedmiot("Matematyka")
        Przedmiot.delete_przedmiot("Polski") 
               
class Test_przedmiot_class_GET_INSTANCE(unittest.TestCase):
    def setUp(self)-> None:
        Przedmiot.przedmiot_list = []
        Przedmiot.instance_list = []
        Przedmiot.create_przedmiot("Matematyka", "Jan Kowalski")
        Przedmiot.create_przedmiot("Polski", "Roman Nowak")
        
    def test_get_instance_failure(self):
         assert_that(Przedmiot.get_instance).raises(ValueError).when_called_with("Szachy")
    
    def test_get_instance_success(self):
         assert_that(Przedmiot.get_instance("Polski")).is_instance_of(Przedmiot)
    
    def tearDown(self):
        Przedmiot.delete_przedmiot("Matematyka")
        Przedmiot.delete_przedmiot("Polski")
        
        
class Test_uczen_class_INIT(unittest.TestCase):
    def setUp(self):
        pass
        
    def tearDown(self):
        pass
    


