from array import *

arr = array('i', [])

n = int(input("Enter Length: "))
for i in range(n):
    x = int(input("Enter Value: "))
    arr.append(x)

print(arr)
