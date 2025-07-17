class HolidayTown:
    def __init__(self, name, holiday_type, ruler):
        self.name = name
        self.holiday_type = holiday_type
        self.ruler = ruler

    def celebrate(self):
        print(f"{self.name} празднует {self.holiday_type} под чутким руководством {self.ruler}!")

        
halloween = HolidayTown("город Хэллоуин", "Хэллоуин", "Джек")
christmas = HolidayTown("город Рождество", "Рождество", "Санта Клаус")
halloween.celebrate()
christmas.celebrate()