from errors import EmptyNameField, EmptyTeacherField, NotUniquePrzedmiot

class Przedmiot():
    przedmiot_list = []
    def __init__(self, nazwa, nauczyciel=""):
            self.nazwa = self._check_if_przedmiot_unique(nazwa)
            self.nauczyciel = nauczyciel
    
    def _check_if_przedmiot_unique(self, nazwa):
        if nazwa in Przedmiot.przedmiot_list:
            raise ValueError("Przedmiot juz jest na liscie")
        Przedmiot.przedmiot_list.append(nazwa)
        return nazwa
            
    @classmethod    
    def create_przedmiot(cls, nazwa, nauczyciel):
        if nazwa in cls.przedmiot_list:
            raise ValueError("Nie mozna dodac - ten przedmiot juz jest na liscie")
        if nazwa == '' and nauczyciel== '':
            raise ValueError("Nie wprowadzono ani nauczyciela ani przedmiotu")
        if nazwa == '':
            raise EmptyNameField
        if nauczyciel == '':
            raise EmptyTeacherField
        else:
            return cls(nazwa, nauczyciel)
    
    def edit_przedmiot(self, nazwa, nauczyciel):
        if nazwa== '':
            new_nazwa = self.nazwa
        if nazwa in Przedmiot.przedmiot_list:
            raise ValueError("Nie mozna edytowac - ten przedmiot juz jest na liscie")
        elif nazwa!='' and nazwa not in Przedmiot.przedmiot_list:
            new_nazwa = nazwa
        if nauczyciel== '':
            new_nauczyciel = self.nauczyciel
        else:
            new_nauczyciel = nauczyciel
        self.nazwa = new_nazwa
        self.nauczyciel = new_nauczyciel

