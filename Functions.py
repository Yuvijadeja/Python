def greet():
    print("Hello")
    print("Good Morning")

def add(x, y):
    z = x + y
    return z

result = add(5, 4)
print(result)

def person(**data):
    print(data)

person(name="Yuvraj", age=26, city="Jamnagar", mob="9662505308")
