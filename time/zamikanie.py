def outher_function(x):
    def inner_function(y):
        return x + y # x  сохраняется в замыкании
    return inner_function


closure = outher_function(10)
print(closure(5)) # выведет 15, так как х=10