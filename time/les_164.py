class HolidayTown:
    
    def __init__(self, name, holiday_type, ruler):
        self.name = name
        self.holiday_type = holiday_type
        self.ruler = ruler
        

    def celebrate(self):
        print(f"{self.name} празднует {self.holiday_type} под руководством {self.ruler}!")
        
# ожидаемое поведение функции, не противоречащее принципу Лисков и родительскому классу
class ChistmasTown(HolidayTown):
    def __init__(self, ruler):
        super().__init__("Рождественский город", "Рождество", ruler)

    def celebrate(self):
        print(f"{self.name} празднует с радостью, подарками и добротой!")
# подставное рождество- нарушающее принцип Лисков, т.е. меняет поведение родителя- дано для примера
class FakeChistmas(ChistmasTown):
    def celebrate(self):
        print(f"{self.name} празднует Рождество... но с криками, страхом и жуткими игрушками!")

fake_xmas = FakeChistmas("Джек Повелитель Тыкв")
fake_xmas.celebrate()
        

#halloween = HolidayTown("город Хэллоуин", "Хэллоуин", "Джек")
#christmas = HolidayTown("город Рождество", "Рождество", "Санта Клаус")
#ester = HolidayTown(input(), input(), input())

#halloween.celebrate()
#ester.celebrate()
