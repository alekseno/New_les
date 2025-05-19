n = int(input())
m = int(input())
x = [['\U0001F333' for j in range(1, m + 1)] for i in range(1, n + 1)]
for row in x:
    print(*row, sep=' ')
    
""" Попросите пользователя ввести два целых числа n и m. Используя вложенные циклы, выведите прямоугольник из символов 🌳 размером n x m"""