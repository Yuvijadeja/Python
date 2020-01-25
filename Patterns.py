for i in range(4):
    for j in range(4):
        print("# ", end="")
    print()

for x in range(4):
    for y in range(x+1):
        print("* ", end="")
    print()

for m in range(4):
    for n in range(4-m):
        print("$ ", end="")
    print()

name = "Yuvraj"
for a in range(len(name)):
    for b in range(a+1):
        print(name[b], end="")
    print()
