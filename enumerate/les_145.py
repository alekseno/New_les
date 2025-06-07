
l = []
for i in range(int(input())):
    r = input()
    l.append(r)

for index, i in enumerate(list(l), start=1):
    print(f"{index}. {i}")