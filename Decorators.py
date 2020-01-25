def div(a, b):
    print(a / b)


def smart_div(f):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return f(a, b)
    return inner


div = smart_div(div)
div(2, 4)
