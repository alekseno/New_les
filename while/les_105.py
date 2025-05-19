secret = 37
count = 0
while (x:= int(input())) != False:
    if x < 37:
        count += 1
        print("Слишком мало!")
    elif x > 37:
        count += 1
        print("Слишком много!")
    elif x == 37:
        count += 1
        print("Код верный, темница открыта!\nКоличество попыток:", count)
        x == False
 