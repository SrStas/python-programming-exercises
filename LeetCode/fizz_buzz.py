n = 3


def fizz_buzz(n):
    res = []
    for i in range(1, n + 1):
        print(i % 3, i % 5)
        if i % 3 == 0 and i % 5 == 0:
            res.append("FizzBuzz")
            continue
        if i % 3 == 0:
            res.append("Fizz")
            continue
        if i % 5 == 0:
            res.append("Buzz")
            continue
        res.append(str(i))
    return res


print(fizz_buzz(15))
