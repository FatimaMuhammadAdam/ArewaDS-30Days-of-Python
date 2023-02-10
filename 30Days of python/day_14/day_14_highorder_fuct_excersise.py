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
