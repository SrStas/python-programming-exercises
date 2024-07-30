# input = [1, 1, 9, 9]
input = [9, 9]


def plusOne(intNumber):
    res = []

    for i in range(len(intNumber) - 1, -1, -1):
        if intNumber[i] < 9:
            intNumber[i] += 1
            return intNumber

        intNumber[i] = 0
    if intNumber[0] == 0:
        intNumber.insert(0, 1)
    return intNumber


print(plusOne(input))

# msd, lsd = recursionAdd(1, 9)

# print(msd, lsd)
