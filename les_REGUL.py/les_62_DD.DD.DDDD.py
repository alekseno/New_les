import re
date = input()
result= re.findall(r'(\d{2}\.\d{2}\.\d{4})', date)
print("Найденные даты:", *result)