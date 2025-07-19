#  используем инкапсуляцию, чтобы защитить важные данные объекта
class Christmas:
    def __init__(self):
        self.__gift_count = 0  # приватный атрибут

    @property # @property — чтобы получить значение
    def gift_count(self):
        return self.__gift_count

    @gift_count.setter # @<имя>.setter — чтобы задать значение (с проверкой)
    def gift_count(self, value):
        if value >= 0:
            self.__gift_count = value
        else:
            print("Нельзя дарить отрицательное количество подарков!")

    def add_gifts(self, count):
        self.gift_count += count

#Теперь Санта может безопасно управлять числом подарков:
xmas = Christmas()
xmas.gift_count = 60
print(xmas.gift_count)  # 100

xmas.gift_count = -5    # Нельзя дарить отрицательное количество подарков!