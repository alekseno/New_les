#рекурсия - вызов функции из самой себя

def a(x):
    print(f"down: x = {x}")
    if x >1:
        a(x-1)
    print(f"up: x = {x}")
a(3)