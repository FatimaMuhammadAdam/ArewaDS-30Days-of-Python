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