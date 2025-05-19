import string
text = "Привет, мир! Как дела?"
table = str.maketrans("", "", string.punctuation) # создает таблицу, где все знаки препинания заменяются на ""(удаляются)
cleaned_text = text.translate(table) # применяет таблицу, удаляя знаки препинания из строки
print(cleaned_text)