nums1 = [1, 2, 2, 1]
nums2 = [2, 2]


def findIntersectionOfArrays(nums1, nums2):
    countDict = {}

    intersectionNums = []
    for i in nums1:
        if i in countDict:
            countDict[i] += 1
        else:
            countDict[i] = 1
    for i in nums2:
        if i in countDict and countDict[i] > 0:
            intersectionNums.append(i)
            countDict[i] -= 1

    return intersectionNums


findIntersectionOfArrays(nums1, nums2)
