"""text = input()
text_01 = text.startswith('Привет')
text_1 = text.endswith("!")
value = text_01 == text_1 == True
print(value)"""

"""Оно начинается с фразы "Привет".
Заканчивается восклицательным знаком "!"""
text = input()
print(text.startswith('Привет') and text.endswith("!"))