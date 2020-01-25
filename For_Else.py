nums = [12, 16, 18, 21, 26]

for n in nums:
    # check that n is divisible by 5
    if n % 5 == 0:
        print(n)
        break
else:
    print("Not found!!")
