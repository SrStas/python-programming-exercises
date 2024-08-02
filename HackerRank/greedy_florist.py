def getMinimumCost(k, c):
    c.sort()
    frDic = {}
    price = 0

    i = 0
    while True:
        if not i < len(c):
            break
        i += 1
    j = 1
    for i in range(len(c) - 1, -1, -1):
        if j > k:
            j = 1
        if j in frDic:
            frDic[j] += 1
        else:
            frDic.update({j: 0})
        priceMultiplier = frDic[j] + 1
        price += c[i] * priceMultiplier

        j += 1
    print(frDic)

    return price


k = 2  # number of friends
c = [2, 5, 6]  # flower prices
n = 3  # number of flowers to buy

c = [1, 3, 5, 7, 9]
k = 3

print(getMinimumCost(k, c))
