class HolidayTown:  # шаблон, описание объекта
    counter = 0
    
    def __init__(self, name, holiday_type, ruler): # конструктор c атрибутами, описывающие объект
        self.name = name
        self.holiday_type = holiday_type
        self.ruler = ruler
        

    def celebrate(self): # функции (методы), которые описывают, что объект умеет делать
        print(f"{self.name} празднует {self.holiday_type} под руководством {self.ruler}!")
        self.counter += 1
        print("счётчик", self.counter)

# объект
halloween = HolidayTown("город Хэллоуин", "Хэллоуин", "Джек")
#christmas = HolidayTown("город Рождество", "Рождество", "Санта Клаус")
#ester = HolidayTown(input(), input(), input())

halloween.celebrate()
#ester.celebrate()
