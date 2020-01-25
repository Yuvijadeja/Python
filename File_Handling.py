f = open("MyData.txt", "r")
# print(f.read()) // it will print whole document
print(f.readline(), end="")
print(f.readline(), end="")

f1 = open("ABC.txt", "a")  # "w" for write and "a" for append
f1.write("Hello")
