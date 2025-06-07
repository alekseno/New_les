
def os_path(disk, *args, sep='\\', **kwargs):
    args = (disk,) + args
 
    if 'trim' in kwargs and kwargs['trim']:
        args = [x.strip() for x in args]
 
    path = sep.join(args)
    return path


p = os_path("F:", "~stepik.org",
            "Добрый, добрый Python (Питон)",
            "39\\p39. Функции.docx",
            sep='/', trim=True
)