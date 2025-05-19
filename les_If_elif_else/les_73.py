object = input().lower()
yes_no = ''
if object != "математика" and object != "физика" and object != "литература" and object != "биология":
    print("Попробуйте себя в разных сферах, чтобы найти своё призвание!")

if object == "математика":
    yes_no = input().lower()
    if yes_no == "да":
        print("Вам подойдет профессия аналитика!")
    else:
        print("Вам подойдет профессия программиста!")

if object == "физика":
    yes_no = input().lower()
    if yes_no == "да":
        print("Вам подойдет профессия астронома!")
    else:
        print("Вам подойдет профессия инженера!")

if object == "литература":
    yes_no = input().lower()
    if yes_no == "да":
        print("Вам подойдет профессия писателя!")
    else:
        print("Вам подойдет профессия редактора!")

if object == "биология":
    yes_no = input().lower()
    if yes_no == "да":
        print("Вам подойдет профессия врача!")
    else:
        print("Вам подойдет профессия эколога!")