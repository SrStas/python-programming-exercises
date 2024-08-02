def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = float("inf")
    for i in range(0, len(arr) - 1):
        diff = abs(arr[i] - arr[i + 1])
        # print(diff)
        if diff < min_diff:
            min_diff = diff

    return min_diff


arr = [-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]
print(minimumAbsoluteDifference(arr))
