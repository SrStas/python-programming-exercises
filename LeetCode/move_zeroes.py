nums = [0, 1, 1, 0, 3, 12]
nums = [0]


def moveZeroes(nums):
    last_non_zero_found_at = 0
    for current in range(len(nums)):
        if nums[current] != 0:
            nums[last_non_zero_found_at] = nums[current]
            last_non_zero_found_at += 1

    # print(last_non_zero_found_at)
    for i in range(last_non_zero_found_at, len(nums)):
        nums[i] = 0

    return nums


numsMoved = moveZeroes(nums)

print(numsMoved)
