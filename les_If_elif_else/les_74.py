dilivery, weight, distance = input().split()
if dilivery == "обычная":
    if float(weight) <= 5:
        print("Стоимость доставки: 200 рублей.")
    elif 5.01 <= float(weight) <= 20:
        print("Стоимость доставки: 500 рублей.")
    elif float(weight)> 20:
        print("Стоимость доставки: 1000 рублей.")
if dilivery == "срочная":
    if int(distance) <= 100:
        if float(weight) <= 5:
            print("Стоимость доставки:", round((200 * 0.1) + 200), "рублей.")
        elif 5.01 <= float(weight) <= 20:
            print("Стоимость доставки:", round((500 * 0.1) + 500), "рублей.")
        elif float(weight) > 20:
            print ("Стоимость доставки:", round((1000 * 0.1) + 1000), "рублей.")
    if int(distance) > 100:
        if float(weight) <= 5:
            print("Стоимость доставки:", round((200 * 0.15) + 200), "рублей.")
        elif 5.01 <= float(weight) <= 20:
            print("Стоимость доставки:", round((500 * 0.15) + 500), "рублей.")
        elif float(weight) > 20:
            print ("Стоимость доставки:", round((1000 * 0.15) + 1000), "рублей.")
