import math
result =  list(map(int, input().split()))	
l = []
for i in result:
    p = int(i) - (int(i) * 0.10)
    l.append(math.floor(p))
print(l)


# 100 250 30 75