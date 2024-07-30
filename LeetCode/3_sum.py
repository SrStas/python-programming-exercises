def sum_of_3_btutforce(nums):
    nums.sort()
    res = []
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if not (i != j and i != k and j != k):
                    continue
                # print(i, j, k)
                if nums[i] + nums[j] + nums[k] == 0:
                    tmpList = [nums[i], nums[j], nums[k]]
                    tmpList.sort()
                    if tmpList not in res:
                        res.append(tmpList)

    return res


def sum_of_3(nums):
    nums.sort()
    result = []
    n = len(nums)

    for i in range(n):
        # Skip duplicate elements to avoid duplicate triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates for the second element
                while left < right and nums[left] == nums[left + 1]:
                    left += 1

                # Skip duplicates for the third element
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < 0:
                left += 1
            else:
                right -= 1

    return result


nums = [-1, 0, 1, 2, -1, -4]
# nums = [0, 0, 0, 0, 0, 0, 0, 0, 0]

print(sum_of_3(nums))
