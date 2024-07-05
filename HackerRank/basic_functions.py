myvar = 42


def test_function():
    print("Test Function")


def loops():
    print("Enter your n:")
    n = int(input())
    if n >= 0:
        for item in range(n):
            print(item * item)


def is_leap(year):
    leap = False

    # Write your logic here
    if (year % 4) == 0:
        leap = True
        if (year % 100) == 0:
            leap = False
            if (year % 400) == 0:
                leap = True

    return leap
