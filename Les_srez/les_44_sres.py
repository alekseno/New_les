x = input()
length = len(x)
b = len(x) // 2

for i in range (len(x)):
    if len(x) % 2 != 0:
        value = False
        break 
    if  x[:b] == x[-b:]:
        value = True
    else:
            value = False
print(value)

"""Напишите программу, которая проверяет, является ли строка симметричной. Симметричная строка — это строка, первая половина которой совпадает со второй (например: "abcdabcd").

Sample Input:
abba

Sample Output:
False"""