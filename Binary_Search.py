# list must be sorted in binary search
pos = -1


def search(lst, n):
    l = 0
    u = len(lst) - 1

    while l <= u:
        mid = (l + u) // 2  # "//" will give only integer value
        if lst[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False


lst = [2, 6, 8, 9, 12, 150, 250, 452, 658, 981, 1023, 1564]

if search(lst, 1564):
    print("Found at ", pos)
else:
    print("Not found")
