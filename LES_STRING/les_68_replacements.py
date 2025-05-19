s = "hello world"

replacements = str.maketrans({"h": "H", "e": "E", "o": "O"}) #функция maketrans() создает сопоставление символов с их заменами.
res = s.translate(replacements) # Метод translate() применяет сопоставление к строке, эффективно заменяя все указанные символы.
print(res)