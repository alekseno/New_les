numbers = [-1, 0, 2, 4] 
for num in numbers: 
    if (positive := num) > 0: 
        print(positive) 
        break 
    # ищем первое положительное число и завершаем итерацию
 # 
print(type(numbers))