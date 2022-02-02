from errors import EmptyNameField, EmptyTeacherField, NotUniquePrzedmiot


class Przedmiot():
    przedmiot_list = []
    instance_list = []
    
    def __init__(self, nazwa, nauczyciel=""):
            self.nazwa = self._check_if_przedmiot_unique(nazwa)
            self.nauczyciel = nauczyciel
            Przedmiot.instance_list.append(self)
    
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
        
    @classmethod
    def edit_przedmiot(cls,staraNazwa, nazwa, nauczyciel):
        if staraNazwa not in Przedmiot.przedmiot_list:
            raise ValueError("Nie ma takiego przedmiotu")
        for item in Przedmiot.instance_list:
                if item.nazwa == staraNazwa:
                    if nazwa== '':
                        new_nazwa = item.nazwa
                    if nazwa in Przedmiot.przedmiot_list:
                        raise ValueError("Nie mozna edytowac - ten przedmiot juz jest na liscie")
                    elif nazwa!='' and nazwa not in Przedmiot.przedmiot_list:
                        new_nazwa = nazwa
                    if nauczyciel== '':
                        new_nauczyciel = item.nauczyciel
                    else:
                        cls.przedmiot_list.remove(staraNazwa)
                        cls.przedmiot_list.append(new_nazwa)
                        new_nauczyciel = nauczyciel
                    item.nazwa = new_nazwa
                    item.nauczyciel = new_nauczyciel
        
    @staticmethod        
    def delete_przedmiot(nazwa):
        if nazwa not in Przedmiot.przedmiot_list:
            raise ValueError("Nie mozna usunac - ten przedmiot nie istnieje")
        else:
            for item in Przedmiot.instance_list:
                if item.nazwa == nazwa:
                    del item 
            Przedmiot.przedmiot_list.remove(nazwa)
    
    @classmethod
    def get_przedmiots(cls):
        tablica_przed_plus_nauczyciel = []
        for item in Przedmiot.instance_list:
            tablica_przed_plus_nauczyciel.append(f"{item.nazwa}, {item.nauczyciel}")
        return tablica_przed_plus_nauczyciel
    
    @classmethod
    def get_instance(cls, name):
        if name not in Przedmiot.przedmiot_list:
            raise ValueError("Nie ma takiego przedmiotu")
        for item in Przedmiot.instance_list:
            if item.nazwa == name:
                return item
            
    
    @classmethod
    def get_nauczyciel(cls, name):
        if name not in Przedmiot.przedmiot_list:
            raise ValueError("Nie ma takiego przedmiotu")
        for item in Przedmiot.instance_list:
            if item.nazwa == name:
                return item.nauczyciel