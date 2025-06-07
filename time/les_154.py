# -----Измерение времени выполнения операции
import time

start_time = time.time()


import string
text = "Привет, мир! Как дела?"
table = str.maketrans("", "", string.punctuation) # создает таблицу, где все знаки препинания заменяются на ""(удаляются)
cleaned_text = text.translate(table) # применяет таблицу, удаляя знаки препинания из строки
print(cleaned_text)

total = 0 
for i in range(1000000): 
    total += i 
end_time = time.time() 

print(f"Время выполнения: {end_time - start_time} секунд") 