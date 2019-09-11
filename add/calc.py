def add(x: int, y: int) -> int:
    if type(x) is int and type(y) is int:
        return x + y
    else:
        raise MyException

class MyException(Exception):
    pass
