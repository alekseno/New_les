result = [i.split() for i in input().split(",")]
l = [list(map(int, x)) for x in result]
tt = []
for i in range(len(l)):
    inner = []
    for j in l[i]:
        if j < 50:
            inner.append(str(j))
            
        if j >= 50:
            continue
    tt.append(inner)
k = []
for y in tt:
    if (len(y) > 0):
          
          k.append(y)
print(k) 

#print(tt)
#  20 30,  55 60, 5 10 