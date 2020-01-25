def count(lst):
    odd = 0
    even = 0

    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return odd, even


lst = [15, 25, 36, 48, 69, 56, 87, 52, 13, 54, 63]
odd, even = count(lst)

print("Odd: {} Even: {}".format(odd, even))
