try:
    leight = int(input()) # длина реки
    name = input()

    result = (leight, name)
    match leight:
        case y if 0 < y < 500:
            print("Это короткая материковая река.")
        case y if 500 <= y <= 2000:
            print("Это река средней длины на материке.")
        case y if y > 2000:
            print("Это длинная материковая река.")
except ValueError:
    print("'Неизвестный тип реки или некорректная длина.")