complex = input().lower()
mean = ''
if complex == "двигатель":
    mean = int(input())
    if mean < 30:
        print("Критически низкий уровень топлива!")
    if 30 <= mean <=70:
        print("Заправьте двигатель для продолжения.")
    elif mean > 70:
        print("Топливо в норме, продолжайте миссию.")
    
if complex == "кислород":
    mean = int(input()) 
    if mean < 50: 
        print("Кислорода мало, проверьте фильтры!")
    elif 50 <= mean <= 80:
        print("Следите за системой подачи кислорода.") 
    elif mean > 80:
        print("Уровень кислорода в норме.")
    
if complex == "защита":
    mean = input() 
    if mean == "да":
        print("Система защиты активирована.")
    elif mean == "нет":
        print("Всё спокойно, можно расслабиться.")
    elif mean !="да" and mean != "нет":
        print("Неверный ввод, проверьте систему защиты!")

if complex != "двигатель" and complex != "кислород" and complex != "защита":
        print("Такой системы не существует, проверьте еще раз!")
        
         