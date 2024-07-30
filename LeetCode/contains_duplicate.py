nums = [1, 2, 3, 1]


def containDuplicate(nums):
    arrayDictionary = {}
    for i in range(len(nums)):
        if str(nums[i]) in arrayDictionary:
            print("key exist")
            return True
        else:
            arrayDictionary[str(nums[i])] = 1

    return False


containsDuplicate = containDuplicate(nums)
print(containsDuplicate)
