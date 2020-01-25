def fib(n):
    f = 0
    s = 1
    print(f)
    print(s)

    for i in range(2, n):
        a = f + s
        f = s
        s = a
        print(a)


fib(10)
