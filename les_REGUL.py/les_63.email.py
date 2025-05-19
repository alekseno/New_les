import re
mail = input()
pattern = r"[\w\-]+@[\w\-]+\.\w+"
result = re.fullmatch(pattern, mail)
print("Email корректен." *bool(result) + "Email некорректен."*(not(bool(result))))


""" 
например, example@mail.com
Вывод: "Email корректен." или "Email некорректен."

Не используйте условные операторы, если Вы их уже проходили.

Подсказка: re.fullmatch()
"""