class ChristmasTown:
    def __init__(self):
        self.name = "Рождественский город"
        self._elves = ["Снежинка", "Печенька"]
        self.__magic = True
x = ChristmasTown()
print(x.name)  # нет ошибки
print(x._elves) # доступ возможен
print(x.__magic) #  ошибка

 # доступ к переменным. Переменная с __ защищена магическим образом(меняется- мы этого не видим). При выхове- ошибка AttributeError: 'ChristmasTown' object has no attribute '__magic'

 # переменная с _ - можно получить доступ, но не желательно

 # Переменная без _ - можно получить доступ