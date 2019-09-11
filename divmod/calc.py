def mydivmod(x: int, y: int) -> int:
    if y != 0:
        q = x // y
        mod = x % y
        return (q, mod)
    else:
        return (0, 0)

def mydivmod2(x: int, y: int) -> int:
    try:
        return divmod(x, y)
    except ZeroDivisionError:
        return (0, 0)
