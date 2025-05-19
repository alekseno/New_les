import re
nn = input()
pattern = r"[\w]+"
result = re.fullmatch(pattern, nn)
print(bool(result))