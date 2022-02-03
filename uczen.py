from pyparsing import PrecededBy
from errors import EmptyNameField, EmptyTeacherField, NotUniquePrzedmiot
from przedmiot import Przedmiot

class Uczen():
    instance_list = []
    id = 0
    id_oceny = 0
    all_oceny = []
    all_uwagi = []
    def __init__(self, imie: str, nazwisko: str, oceny: list=True, uwagi: list=True):
            if oceny:
                self.oceny = []
            if uwagi:
                self.uwagi = []
            self.imie = imie
            self.nazwisko = nazwisko
            self.id = Uczen.id
            self.uwagi = uwagi
            if type(oceny) is not list:
                if oceny == '':
                    self.oceny = []
                if oceny != '':
                    oceny_arr = []
                    oceny_arr.append(oceny)
                    self.oceny = oceny_arr    
            else:
                self.oceny = oceny
                
            if type(uwagi) is not list:
                if uwagi == '':
                    self.uwagi = []
                if uwagi != '':
                    uwagi_arr = []
                    uwagi_arr.append(uwagi)
                    self.uwagi = uwagi_arr    
            else:
                self.uwagi = uwagi
            Uczen.id += 1
            Uczen.instance_list.append(self)

        
    @classmethod    
    def create_uczen(cls, imie, nazwisko, oceny, uwagi):
        if imie == '' or nazwisko== '':
            raise ValueError("Nie wprowadzono ani imienia ani nazwiska")
        return cls(imie, nazwisko, oceny, uwagi)
        
    @classmethod
    def edit_uczen(cls,_id, imie, nazwisko):            
        for uczen in Uczen.instance_list:
            if uczen.id == _id:
                edited_uczen  = uczen
                if imie == "":
                    imie = edited_uczen.imie
                if nazwisko == "":
                    nazwisko = edited_uczen.nazwisko
                edited_uczen.imie = imie
                edited_uczen.nazwisko = nazwisko
                return f"Nowe dane: imie:{uczen.imie}, nazwisko:{uczen.nazwisko}"
        raise ValueError("Nie ma ucznia o podanym id - nie mozna edytowac")
        
    @classmethod        
    def delete_uczen(cls,_id):
        uczen_do_usuniecia = Uczen.get_instance(_id)
        if type(uczen_do_usuniecia)!=str:
                del uczen_do_usuniecia
                return "Usunięto ucznia"            
        else:
            return uczen_do_usuniecia
        
    @classmethod
    def get_oceny(cls, _id):
        uczen = Uczen.get_instance(_id)
        if type(uczen)!=str:
            return uczen.oceny
        else:
            return uczen       
    
    @classmethod
    def get_uwagi(cls, _id):
        uczen = Uczen.get_instance(_id)
        if type(uczen)!=str:
            return uczen.uwagi
        else:
            return uczen            
    
    @classmethod
    def get_instance(cls, _id):
        for item in Uczen.instance_list:
            if item.id == _id:
                return item
        return "Nie ma instance o podanym id"
    
    @classmethod
    def get_wszyscy_uczniowie(cls):
        klasa = []
        for item in Uczen.instance_list:
            klasa.append(f"id:{item.id}, imie:{item.imie}, nazwisko:{item.nazwisko}, oceny:{item.oceny}, uwagi:{item.uwagi}")
        return klasa
    
    @staticmethod
    def testInput(a,b,c):
        if "" in (a, b, c):
            raise ValueError("Jeden z atrybutów jest pusty")
        if b not in Przedmiot.przedmiot_list:
            raise ValueError("Nie ma takiego przedmiotu - nie mozna wystawic oceny")           
        if c<1 or c>6:
            raise ValueError("Ocena nie moze byc wieksza od 6 lub mniejsza od 1")   
        return 1             
      
    @staticmethod
    def dodaj_ocene(id_ucznia, przedmiot, wartosc):
        Uczen.testInput(id_ucznia, przedmiot, wartosc)
        uczen_do_oceny = Uczen.get_instance(id_ucznia)       
        id_oceny = Uczen.id_oceny
        nauczyciel = Przedmiot.get_nauczyciel(przedmiot)
        new_ocena = {
                    'id_ucznia': id_ucznia,
                    'id_oceny': id_oceny,
                    'przedmiot': przedmiot,
                    'nauczyciel': nauczyciel,
                    'wartosc': wartosc
                }
        Uczen.id_oceny += 1
        uczen_do_oceny.oceny.append(new_ocena)
        Uczen.all_oceny.append(new_ocena)
        return new_ocena

    @staticmethod
    def delete_ocena(id_oceny):
        for item in Uczen.all_oceny:
            if item['id_oceny'] == id_oceny:
                Uczen.all_oceny.remove(item)
                edytowany_uczen=Uczen.get_instance(item['id_ucznia'])
                edytowany_uczen.oceny.remove(item)
                return "Usunięto ocenę"
        raise ValueError("Nie ma oceny o podanym id - nie mozna usunac")
            
    @staticmethod
    def edit_ocena(id_oceny, wartosc):
        if wartosc<1 or wartosc>6:
            raise ValueError("Ocena nie moze byc wieksza od 6 lub mniejsza od 1")   
        for item in Uczen.all_oceny:
            if item['id_oceny'] == id_oceny:
                edytowany_uczen=Uczen.get_instance(item['id_ucznia'])
                index = edytowany_uczen.oceny.index(item)
                edytowany_uczen.oceny[index]['wartosc']=wartosc
                item['wartosc']=wartosc
                return "Edycja oceny zakończona"
        raise ValueError("Nie ma oceny o podanym id - nie mozna edytowac")
            