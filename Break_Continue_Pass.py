av = 5
x = int(input("Quantity:"))
i = 1
while i <= x:
    if i > av:
        break
    print("Candy")
    i += 1

print("Bye")

for j in range(11):
    if j % 3 == 0:
        continue
    print(j)

age = 17
if age < 18:
    pass
else:
    print("Vote now!")