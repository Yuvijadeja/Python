n = 8
for i in range(2, n):
    if n % i == 0:
        print("Not Prime Number")
        break
else:
    print("Prime Number")
