import re 

text = "Я люблю Python и Java" 
result = re.sub(r"Python|Java", "программирование", text) 
print(result)