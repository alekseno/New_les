import re
text = input()

result = re.sub(r'a', '97', text)
text = result
result= re.sub(r'o', '0', text)
print(result)

"""
Запрашивает у пользователя сообщение.
Заменяет все буквы 'a' в сообщении на их числовой код.
Заменяет все буквы 'o' на символ '0'.
Выводит измененное сообщение на экран."""

#print("Email корректен." *bool(result) + "Email некорректен."*(not(bool(result))))


"""print(ord("m"))
print(chr(100))"""