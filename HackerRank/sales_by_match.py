n = 7
ar = [1, 2, 1, 2, 1, 3, 2]

ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]


def sockMerchant(n, ar):
    dic = {}
    for i in range(n):
        if ar[i] in dic:
            dic[ar[i]] += 1
        else:
            dic[ar[i]] = 1
    pairs = 0
    for key in dic:
        pairs = pairs + dic[key] // 2

    return dic


print(sockMerchant(n, ar))
