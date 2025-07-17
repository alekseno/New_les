def decorator_function(func):
    def wrapper():
        print("До вызова функции")
        func()
        print("После вызова функции")
    return wrapper


@decorator_function # @decorator_function — это синтаксический сахар, эквивалентный записи: say_hello = decorator_function(say_hello).
def say_hello():
    print("Привет")

say_hello()