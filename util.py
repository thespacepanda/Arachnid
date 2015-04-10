def printing(message):
    try:
        print(message)
    except UnicodeEncodeError:
        print("Hit a character I could not print!")

def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        next(cr)
        return cr
    return start

def sending(target, collection):
    for item in collection:
        printing("This is {} in {}".format(item, collection))
        target.send(item)
