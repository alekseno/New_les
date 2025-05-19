health = int(input()) # здоровье
has_weapon = input().lower() == "да" # есть оружие
has_armor = input().lower() == "да" # есть броня

if health > 50:
    if (has_weapon or has_armor) == 1:
        print("Готов к сражению!")
    elif (has_weapon and has_armor)== 0:
        print("Не стоит сражаться без экипировки!")

if health <= 50:
    if has_weapon == 0 and has_armor == 0:
      print("Не готов к сражению!")
    elif has_weapon == 1 and has_armor == 1:
        print("Не стоит рисковать, но у тебя есть все шансы выжить!")
    elif has_weapon == 1 or has_armor == 1:
        print("Не стоит рисковать!")
