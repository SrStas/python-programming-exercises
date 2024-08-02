s = "aba"
n = 10


def repeatingString(s, n):
    res = 0
    tempResToMultiply = 0
    reminderRes = 0
    remainder = n % len(s)
    multiplayer = n // len(s)

    for i in range(0, len(s)):
        if s[i] == "a":
            tempResToMultiply += 1
            if i < remainder:
                reminderRes += 1
    res = tempResToMultiply * multiplayer + reminderRes

    return res


print(repeatingString(s, n))
