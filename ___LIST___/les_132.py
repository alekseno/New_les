h = int(input())
w = int(input())
result = [["*" for j in range(w)] for i in range(h)]
for row in result:
    print(*row, sep='')
#print(*result, sep='\n')