# num = [2,2,1]
nums = [4, 1, 2, 1, 2]


def findTheSingleNumber(nums):
    dictionaryTemp = {}
    for i in range(len(nums)):
        if nums[i] in dictionaryTemp:
            print("exists")
            dictionaryTemp[nums[i]] += 1
        else:
            dictionaryTemp[nums[i]] = 1

    for i in dictionaryTemp:
        if dictionaryTemp[i] == 1:
            print(i)
        # print(dictionaryTemp[i])
    return


theNumber = findTheSingleNumber(nums)
# print(theNumber)
