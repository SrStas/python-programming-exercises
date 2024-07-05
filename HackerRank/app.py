import basic_functions
# from basic_functions import test_function, loops

from math import pi, tau
import fractions


def get_even_numbers():
    for number in range(1, 11):
        print(number * 2)


def x_print(requested_output, quantity):
    for _ in range(quantity):
        print(requested_output)


tv_show = {"title": "Star Trek", "seasons": 15, "initial_release": 2000}


def print_show_info(show):
    print(f"{show['title']} ({show['initial_release']}) - {show['seasons']}")


# get_even_numbers()

# x_print("hello world", 4)

# print_show_info(tv_show)

# print(pi * 5**2)

# fraction = fractions.Fraction(2.25)
# print(fraction)


# loops()
year = int(input())
isLeap = basic_functions.is_leap(year)
print(isLeap)
