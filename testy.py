import unittest
from unittest import mock
from unittest.mock import Mock, patch
from nose2.tools import params
from main import get_data
from przedmiot import Przedmiot
from assertpy import assert_that
from errors import EmptyNameField, EmptyTeacherField, NotUniquePrzedmiot
from uczen import Uczen
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
        
class Test_przedmiot_class_GET_NAUCZYCIEL(unittest.TestCase):
    def test_get_nauczyciel_failure(self):
        Przedmiot.przedmiot_list = ['Angielski']
        assert_that(Przedmiot.get_nauczyciel).raises(ValueError).when_called_with('Przyroda')
        
    def test_get_nauczyciel_success(self):
        Przedmiot.przedmiot_list = ['Angielski']
        mock_instance_list = Mock(nazwa="Angielski", nauczyciel="Jan Kowalski")
        Przedmiot.instance_list = [mock_instance_list]
        assert_that(Przedmiot.get_nauczyciel("Angielski")).is_equal_to('Jan Kowalski')
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
        
        
class Test_uczen_class_CREATE_UCZEN(unittest.TestCase):
    def test_create_success_oneGrade_oneUwaga(self):
        assert_that(Uczen.create_uczen('Test','User',6,"Uwaga")).is_instance_of(Uczen)
   
    def test_create_success_noGrade_noUwaga(self):
        assert_that(Uczen.create_uczen('Test','User','','')).is_instance_of(Uczen)    
   
    def test_create_success_multipleGrade_multipleUwaga(self):
        assert_that(Uczen.create_uczen('Test','User',[6,2],['Lorem','Ipsum'])).is_instance_of(Uczen)    
    
    def test_create_failure(self):
        assert_that(Uczen.create_uczen).raises(ValueError).when_called_with("","",'','')


class Test_uczen_class_GET_WSZYSCY_UCZNIOWIE(unittest.TestCase):
    def test_get_wszyscy(self):
        mock_instance = Mock(name = 'instance_list',  id= 0, imie= "Test", nazwisko="User",oceny= 3,uwagi= "Brak uwag")
        mock_instance_list = [mock_instance]
        Uczen.instance_list = mock_instance_list     
        assert_that(Uczen.get_wszyscy_uczniowie()).is_equal_to(['id:0, imie:Test, nazwisko:User, oceny:3, uwagi:Brak uwag'])

class Test_uczen_class_EDIT_UCZEN(unittest.TestCase):
    def setUp(self)-> None:
        mock_instance = Mock(name = 'instance_list',  id= 0, imie= "Test", nazwisko="User",oceny= 3,uwagi= "Brak uwag")
        mock_instance_list = [mock_instance]
        Uczen.instance_list = mock_instance_list  
        
    def test_edit_uczen_success_name_and_surname(self):
        assert_that(Uczen.edit_uczen(0,"lorem","ipsum")).is_equal_to('Nowe dane: imie:lorem, nazwisko:ipsum')

    def test_edit_uczen_success_surname(self):
        assert_that(Uczen.edit_uczen(0,"","ipsum")).is_equal_to('Nowe dane: imie:Test, nazwisko:ipsum')
    
    def test_edit_uczen_success_none(self):
        assert_that(Uczen.edit_uczen(0,"","")).is_equal_to('Nowe dane: imie:Test, nazwisko:User')
           
    def test_edit_uczen_failure(self):
        assert_that(Uczen.edit_uczen).raises(ValueError).when_called_with(1,"lorem","ipsum")
    
    
    def tearDown(self):
        Uczen.instance_list = []
        
class Test_uczen_class_GET_INSTANCE(unittest.TestCase):
    def setUp(self):
        mock_instance = Mock(name = 'instance_list', id=0, side_effect=ValueError)
        Uczen.instance_list = [mock_instance]
        
    def test_get_instance_success(self):
        mock_instance = Mock(name = 'instance_list', id=0, side_effect=ValueError)
        Uczen.instance_list = [mock_instance]
        assert_that(Uczen.get_instance(0)).is_equal_to(mock_instance)

    def test_get_instance_failure(self):
        assert_that(Uczen.get_instance(1)).is_equal_to('Nie ma instance o podanym id')

class Test_uczen_class_DELETE_UCZEN(unittest.TestCase):    
    def test_delete_uczen_success(self):
        mock_instance = Mock(name = 'instance_list', id=0)
        Uczen.instance_list = [mock_instance]
        assert_that(Uczen.delete_uczen(0)).is_equal_to("Usunięto ucznia")

    def test_delete_uczen_failure(self):
        assert_that(Uczen.delete_uczen(100)).is_equal_to("Nie ma instance o podanym id")
        
class Test_uczen_class_GET_UWAGI(unittest.TestCase):
    @patch('uczen.Uczen.get_instance')
    def test_get_uwagi_success(self, get_instance_mock):
        get_instance_mock.return_value.uwagi = "Przykładowa uwaga"
        assert_that(Uczen.get_uwagi(0)).is_equal_to("Przykładowa uwaga")
    
    @patch('uczen.Uczen.get_instance')
    def test_get_uwagi_failure(self, get_instance_mock):
        get_instance_mock.return_value = "Nieistniejace instance"
        assert_that(Uczen.get_uwagi(0)).is_equal_to("Nieistniejace instance")
        
class Test_uczen_class_GET_OCENY(unittest.TestCase):
    @patch('uczen.Uczen.get_instance')
    def test_get_oceny_success(self, get_instance_mock):
        get_instance_mock.return_value.oceny = 6
        assert_that(Uczen.get_oceny(0)).is_equal_to(6)
    
    @patch('uczen.Uczen.get_instance')
    def test_get_oceny_failure(self, get_instance_mock):
        get_instance_mock.return_value = "Nieistniejace instance"
        assert_that(Uczen.get_oceny(0)).is_equal_to("Nieistniejace instance")
        
class Test_uczen_class_TEST_INPUT(unittest.TestCase):
    def test_uczen_test_fail_empty_fields(self):
        assert_that(Uczen.testInput).raises(ValueError).when_called_with('','przyroda','')
    
    def test_uczen_test_fail_nonexistent_przedmiot(self):
        Przedmiot.przedmiot_list = ['Angielski']
        assert_that(Uczen.testInput).raises(ValueError).when_called_with(1,'przyroda',3)
    
    def test_uczen_test_fail_grade_out_of_range(self):
        Przedmiot.przedmiot_list = ['Angielski']
        assert_that(Uczen.testInput).raises(ValueError).when_called_with(1,'Angielski',8)
    
    def test_uczen_test_success(self):
        Przedmiot.przedmiot_list = ['Angielski']
        assert_that(Uczen.testInput(1, 'Angielski',5)).is_equal_to(1)
        
class Test_uczen_class_DODAJ_OCENE(unittest.TestCase):
    @patch('uczen.Uczen.testInput')
    @patch('uczen.Uczen.instance_list')
    @patch('przedmiot.Przedmiot.get_nauczyciel')
    def test_dodaj_ocene_success(self, mock_testInput, mock_getInstanceOfStudent, mock_get_nauczyciel):
        uczen_testowy = Uczen("Darek","Nowak","","")
        mock_testInput.return_value = 1
        Uczen.id_oceny = 0
        mock_getInstanceOfStudent.return_value.id = 1
        Przedmiot.przedmiot_list = ["Angielski"]
        mock_get_nauczyciel.return_value = "Jan Kowalski"
        assert_that(Uczen.dodaj_ocene(0,"Angielski",5)).is_equal_to(
                    {'id_oceny': 0,
                    'przedmiot': "Angielski",
                    'nauczyciel': "Jan Kowalski",
                    'wartosc': 5})