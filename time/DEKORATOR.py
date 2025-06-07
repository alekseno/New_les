import time
# универсальный декоратор для подсчета времени за сколько отработает функция
def test_time(fn):
    def wrapper(*args, **kwargs):
        st = time.time()
        res = fn(*args, **kwargs)
        dt = time.time() - st
        print(f"Время работы: {dt} сек")
        return res
 
    return wrapper

#-------------------------------------------


def func_decorator(func):
    def wrapper():
        print("------ что-то делаем перед вызовом функции ------")
        func()
        print("------ что-то делаем после вызова функции ------")
 
    return wrapper


def some_func():
    print("Вызов функции some_func")

f = func_decorator(some_func)
f()


#https://stepik.org/lesson/567062/step/1?unit=561336