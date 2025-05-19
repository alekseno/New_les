name_heroes = input()
level = input()
house = input()
print(name_heroes.isalpha() and level.isdigit() and (house.isalpha() or house.isspace()))
 



# isalpha() - только буквы
# .isspace() - только пробелы
# .isdigit() - только цифры
"""Имя героя — должно содержать только буквы.
Уровень героя — должно быть числом.
Замок героя — название замка, должно содержать только буквы либо состоять из одних пробелов, последнее будет означать, что замок скрыт туманом войны."""