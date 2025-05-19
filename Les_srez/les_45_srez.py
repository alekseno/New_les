x = input()
a = int(input())
b = int(input())
xx = x[:a] + x[b+1:]
print(xx)

"""Напишите программу, которая принимает строку и два числа a и b (каждое вводится с новой строки). Программа должна удалить из строки символы с индексами от a до b (включительно).

Sample Input:
abcdefghij
2
5
Sample Output:
abghij"""