import re
#name = input()
pattern = "[aeiouy]+"

a = ord("a")
A = ord("A")
e = ord("e")
E = ord('E')
#repl = ""
result = re.sub(pattern, repl, "ahjjeuyytti")
print(result)
