nums = [1, 2, 3, 4, 5, 6, 7]
k = 9


def rotateArrayByK(array, k):
    if k > len(nums):
        k = k % len(array)
        print(k)
    resArray = []
    length = len(array)
    print(length)

    for i in range((len(array) - k), len(array)):
        resArray.append(array[i])

    for i in range(len(array) - k):
        resArray.append(array[i])

    for i in range(len(array)):
        array[i] = resArray[i]

    return array


resArray = rotateArrayByK(nums, k)

print(resArray)
