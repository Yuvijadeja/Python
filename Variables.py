num = 5
# get the address of num variable
print(id(num))

# Address actually refers to the value not to the var name
a = num
print(id(a))
print(id(5))

print(type(a))

i = 5.5
j = int(i)
print(j)

print(range(10))
y = list(range(2, 10, 2))
print(y)

# Dictionary
d = {'Yuvi': 'J7 Max', 'Jigs': 'M20'}
print(d)
print(d.keys())
print(d.values())
print(d['Yuvi'])
print(d.get('Jigs'))