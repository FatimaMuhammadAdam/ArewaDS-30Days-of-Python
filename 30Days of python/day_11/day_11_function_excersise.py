#importing labries
import math
import re
import sys

sys.path.append("data")
import countries_data
#Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(t, y):
    return t + y

#Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r):
    return 3.14*r**2
# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(arr):
    sum_of_nums = 0
    for i in arr:
        if isinstance(i, int):
            sum_of_nums += i
    return sum_of_nums


# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit
def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


#Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ["September", "October", "November"]:
        print("Autumn")
    if month in ["December", "January", "February"]:
        print("Winter")
    if month in ["March", "April", "May"]:
        print("Spring")
    else:
        print("Summer")


# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    return m


# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_eqn(a, b, c):
    D = b * b - 4 * a * c
    X1 = (-b + D) / (2 * a)
    X2 = (-b - D) / (2 * a)
    print(X1, X2)


# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for i in lst:
        print(i)


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(a):
    return a[::-1]


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capital_list_terms(a):
    for i in a:
        a[a.index(i)] = i.capitalize()
    return a


# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(mutable, tba):
    mutable.append(tba)
    return mutable


# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(mutable, tbr):
    mutable.remove(tbr)
    return mutable


# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range
def sum_of_numbers(high):
    sum_of_numbers = 0
    for i in range(high + 1):
        sum_of_numbers += i
    return sum_of_numbers


# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(high):
    sum_of_odd_nums = 0
    for i in range(high + 1):
        if i % 2 == 1:
            sum_of_odd_nums += i
    return sum_of_odd_nums


# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(high):
    sum_of_even_nums = 0
    for i in range(high + 1):
        if i % 2 == 0:
            sum_of_even_nums += i
    return sum_of_even_nums


# Level 2

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number

def evens_and_odds(high):
    odds = 0
    evens = 0
    for i in range(high + 1):
        if i % 2 == 0:
            evens += i
        else:
            odds += i
    print(odds, evens)


# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(fac):
    fact = 1
    for i in range(fac + 1):
        fact *= i
    return fact


# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(check):
    if check:
        return True
    else:
        return False


# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation)
def mean(dataset):
    return sum(dataset) / len(dataset)


def median(dataset):
    data = sorted(dataset)
    index = len(data) // 2

    if len(dataset) % 2 != 0:
        return data[index]

    return (data[index - 1] + data[index]) / 2


def mode(dataset):
    frequency = {}

    for value in dataset:
        frequency[value] = frequency.get(value, 0) + 1

    most_frequent = max(frequency.values())

    modes = [key for key, value in frequency.items() if value == most_frequent]

    return modes


def variance(dataset):
    n = len(dataset)
    mean = sum(dataset) / n
    deviations = [(x - mean) ** 2 for x in dataset]
    variance = sum(deviations) / n
    return variance


def stdev(dataset):
    var = variance(dataset)
    std_dev = var ** 0.5
    return std_dev


# Level 3

#Write a function called is_prime, which checks if a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    max_div = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return False
    return True


# Write a functions which checks if all items are unique in the list.
def checK_list(test_list):
    return len(set(test_list)) == len(test_list)


#Write a function which checks if all the items of the list are of the same data type.
def homogeneous_type(seq):
    iseq = iter(seq)
    first_type = type(next(iseq))
    return first_type if all((type(x) is first_type) for x in iseq) else False


def isVar(test):
    return re.match(r"[_a-z]\w*$", test, flags=re.I)


list_data = countries_data.data
total_languages_initial = []
for i in list_data:
    total_languages_initial.extend(i["languages"])
print("Languages = ", len(set(total_languages_initial)))
counts = {}
for i in total_languages_initial:
    counts[i] = counts.get(i, 0) + 1


def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


counts = sort_dict_by_value(counts, True)
for i in list(counts.items())[:20]:
    print(i)
populations = {}
for i in list_data:
    populations[i["name"]] = i["population"]
populations = sort_dict_by_value(populations, True)
for i in list(populations.items())[:20]:
    print(i)