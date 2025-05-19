numbers = [-5, -3, 0, 2, 4, -1] 
for num in numbers: 
    if (positive := num) > 0: 
        print(f"Первое положительное число: {positive}") 
        break 
else: 
    print("Положительных чисел не найдено.") 

