request = {
    'url': "https://proproprogs.ru/",
    'method': "GET", 
    'timeout': 1000
    }

"""match request:
    case {'url': url, 'method': method}:
        print(f"Запрос: url: {url}, method: {method}")
    case _:
        print("неверный запрос")"""



# match case для словарей- важно, чтобы в шаблоне присутствовали ключи (#, url, method)

#match case для списков и кортеджей- в шаблоне указывается то количество элементов, которое ожидается в списке или кортедже

# для проверки на тип данных, конструкция match case выглятит так:
# ---проверка, что данные строки

"""match request:
    case {'url': str() as url, 'method': str(method)}:
        print(f"Запрос: url: {url}, method: {method}")
    case _:
        print("неверный запрос")"""

# --- проверка, что есть 2 обязательных ключа и есть несколько параметров (**kwargs), но их должно быть не более двух

match request:
    case {'url': url, 'method': method, **kwargs} if len(kwargs) <= 2:
        print(f"Запрос: url: {url}, method: {method}")
    case _:
        print("неверный запрос")