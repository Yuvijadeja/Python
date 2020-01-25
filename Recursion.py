# Recursion - Function calling it self
# In python limit for recursion is 1000 (but it can be increase)


def fact(n):
    return n * fact(n-1)


print(fact(5))
