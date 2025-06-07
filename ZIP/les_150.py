name = input().replace(',', '').split()
surname = input().replace(',', '').split()

for name, surname in zip(name, surname):
    print(f"{name} {surname}")

"""Пользователь вводит список имён и список фамилий через запятую. Программа должна вывести полные имена, объединяя соответствующие элементы двух списков."""