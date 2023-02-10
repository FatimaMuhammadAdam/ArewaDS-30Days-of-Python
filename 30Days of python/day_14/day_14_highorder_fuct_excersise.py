countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Exercises: Level 1
#Explain the difference between map, filter, and reduce.
"""map(): function is a built-in function that takes a function and iterable as parameters, 
and its the most simplest build in function in python. What actually map does is iterating over a list

The filter() function calls the specified function which returns boolean for each item of the specified iterable (list).
It filters the items that satisfy the filtering criteria.extracts each element in the sequence for which the function returns True

The reduce() function is defined in the functools module and we should import it from this module. Like map and filter it takes two parameters, a function and an iterable.
However, it does not return another iterable, instead it returns a single value.
The reduce function is a little less obvious in its intent. 
This function reduces a list to a single value by combining elements via a supplied function."""
#Explain the difference between higher order function, closure and decorator
"""higher order function is any function returning different functions depending on the passed parameter.

Closure is a process where by  a nested function to access the outer scope of the enclosing function.
closure is created by nesting a function inside another encapsulating function and then returning the inner function.

A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure. 
Decorators are usually called before the definition of a function you want to decorate."""
#Define a call function before map, filter or reduce, see examples.
def cube(num):
    return num ** 3


def vowel_name(name):
    if name[0] in 'aeiouAEIOU':
        return True
    return False


def sum_of_cubes(num1, num2):
    return num1 + num2


print(list(filter(vowel_name, names)))
print(list(map(cube, numbers)))
reduce=(sum_of_cubes, list(map(cube, numbers)))
print(reduce)

#Use for loop to print each country in the countries list.
for country in countries:
    print(country)
#Use for to print each name in the names list.
for name in names:
    print(name)
#Use for to print each number in the numbers list.
for number in numbers:
    print(number)

#Exercises: Level 2
#Use map to create a new list by changing each country to uppercase in the countries list
upper_countries = list(map (lambda e: e.upper(), countries))
print (upper_countries)

#Use map to create a new list by changing each number to its square in the numbers list
square_numbers = list(map(lambda w: w**w, numbers))
print(square_numbers)

#Use map to change each name to uppercase in the names list
names_upper = list(map (lambda q: q.upper(), names))
print(names_upper)

#Use filter to filter out countries containing 'land'.
countries = list(filter(lambda e:'land' in e, countries))
countries
#Use filter to filter out countries having exactly six characters.
six_char_countries = list(filter(lambda e: len(e)== 6, countries))
six_char_countries
#Use filter to filter out countries containing six letters and more in the country list.
six_more_char_countries = list(filter(lambda e: len(e)>= 6, countries))
six_more_char_countries
#Use filter to filter out countries starting with an 'E'
filtered_countries = list(filter(lambda e: e[0] != 'E', countries))
filtered_countries
#Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
iterators = reduce(lambda x, y: x + y, 
                filter(lambda x: x[0] != 'E', 
                       map(lambda x: x.upper(), countries)))
print(iterators)

#Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

def toString(string):
    return str(string)


def get_string_lists(arr):
    return list(map(toString, arr))


print(get_string_lists(numbers))

#Use reduce to sum all the numbers in the numbers list.
#let import the reduce modules from functools and others labaries
from functools import reduce
import sys

sys.path.append('data')
# noinspection PyUnresolvedReferences
from countries import country_list
# noinspection PyUnresolvedReferences
from countries_data import data
import pprint

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)

#Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
countries = reduce(lambda x, y: x + ', ' + y, countries[:-1]) + ', and ' + countries[-1] + ' are north European countries.'
print(countries)
#Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

keys = []
keys = [i[0] for i in country_list if i[0] not in keys]


def countCountry(csv1):
    return sum([True for i in country_list if i[0].startswith(csv1)])


vals = [countCountry(l) for l in keys]

print(dict(zip(keys, vals)))
#Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folde
def get_first_ten():
    return country_list[:10]

#Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten():
    return country_list[-1:-11:-1]
#Exercises: Level 3
#Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:

# Level 3

pprint.pprint(sorted(data, key=lambda y: y['name']))
pprint.pprint(sorted(data, key=lambda u: u['capital']))
pprint.pprint(sorted(data, key=lambda x: x['population']))

total_languages_initial = []
for u in data:
    total_languages_initial.extend(u["languages"])
# noinspection DuplicatedCode
counts = {}
for i in total_languages_initial:
    counts[i] = counts.get(i, 0) + 1


def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


counts = sort_dict_by_value(counts, True)
final_dict_1 = {}
for i in list(counts.items())[:10]:
    final_dict_1[list(i)[0]] = list(i)[1]
pprint.pprint(sorted(final_dict_1))

pprint.pprint(list(sorted(data, key=lambda x: x['population'], reverse=True))[:10])
