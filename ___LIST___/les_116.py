city = input().split()
print(city[2:5])
print(city[3:8])
y = []
for word in city:
    if word.startswith("М"):
        y.append(word)
print(y)

counter = 0
for i in city:
    if i.startswith("И"):
        counter += 1
print(counter)