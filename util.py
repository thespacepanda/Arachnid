import functools

def flip(func):
    "Returns the given function with the argument order reversed"
    @functools.wraps(func)
    def newfunc(*args):
        return func(*args[::-1])
    return newfunc
