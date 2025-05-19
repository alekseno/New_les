number = input()
num = number.isdigit() # проверка, что введено число. Если да, уходим в цикл
if num == True:
    if 1 <= int(number) < 12:
        print("Привет, малыш!")
    elif 12 <= int(number) <=18:
        print("Привет, подросток!")
    elif 19 <= int(number) <= 65:
        print("Добрый день, взрослый!")
    elif int(number) > 65:
        print("Здравствуйте, уважаемый пенсионер!")
    elif int(number) == 0:
        print("Некорректный ввод")
else:
    print("Некорректный ввод") # введены буквы или отрицательные числа
