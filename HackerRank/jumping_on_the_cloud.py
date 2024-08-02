c = [0, 0, 1, 0, 0, 1, 0]
# c = [0,1,0,0,0,1,0,0]
c = [0, 1, 0, 0, 0, 1, 0]
c = [0, 0, 0, 1, 0, 0]
n = 7


def jumpingOnClouds(c):
    res = 0
    i = 1
    while i < len(c):
        # print(i)
        if i + 1 < len(c) and c[i + 1] == 0:
            i += 2
        elif c[i] == 0:
            i += 1
        res += 1

    return res


print(jumpingOnClouds(c))
