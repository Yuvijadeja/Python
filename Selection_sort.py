def sort(nums):
    for i in range(len(nums)-1):
        minpos = i
        for j in range(i, len(nums)):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp


num = [5, 8, 6, 2, 3, 7]
sort(num)
print(num)
