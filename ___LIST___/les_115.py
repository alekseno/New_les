x = list(map(str, input().split()))
print(x[2:5])
y = []
for word in x:
    if word.startswith("Г"):
        y.append(word)
print(y)
        
counter = 0
for i in x:
    if i.startswith("М"):
        counter += 1
print(counter)

"""Введите имена 8 героев в одну строку через пробел.
С помощью срезов и циклов:
Выведите имена героев на 3-й, 4-й и 5-й позициях.
Найдите героев, чьи имена начинаются на букву "Г".
Посчитайте, сколько героев в списке начинаются на букву "М"."""