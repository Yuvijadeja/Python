from functools import reduce
f = lambda a: a * a

print(f(5))


nums = [2, 5, 6, 8, 9, 15, 62, 35, 87, 92]
even = list(filter(lambda n: n % 2 == 0, nums))
double = list(map(lambda n: n * 2, even))
sum = reduce(lambda a, b: a + b, double)

print(even)
print(double)
print(sum)
