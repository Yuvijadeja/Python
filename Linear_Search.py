pos = -1


def search(lst, n):
    i = 0
    while i < len(lst):
        if lst[i] == n:
            globals()['pos'] = i
            return True
        i += 1
    return False


lst = [5, 8, 6, 9, 2, 3, 7, 10, 12]

if search(lst, 5):
    print("Found at ", pos)
else:
    print("Not found")
