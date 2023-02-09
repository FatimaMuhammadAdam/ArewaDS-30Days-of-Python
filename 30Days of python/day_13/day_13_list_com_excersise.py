#Filter only negative and zero in the list using list comprehension
#numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filter = [h for h in numbers if h<=0]
print(filter)
#Flatten the following list of lists of lists to a one dimensional list :
#list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list = [ h for row in list_of_lists for h in row]
print(flattened_list)
#Using list comprehension create the following list of tuples:
"""[(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

"""
#list_of_tuples = []
#list_of_tuples =([i for i in range(11)]numbers.append((i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5)))

#Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten_list_of_tuples = [[sub2[0].upper(), sub2[0].upper()[:3], sub2[1].upper()] for sub in countries for sub2 in sub]
print(flatten_list_of_tuples)
    
#Change the following list to a list of dictionaries:

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries = [[sub2[0].upper(), sub2[1].upper()] for sub in countries for sub2 in sub]
countries = [d for sub in countries for d in sub]
keys = ["country", "city"]
dictionary =[{keys[0]: countries[idx], keys[1]: countries[idx + 1]} for idx in range(0, len(countries), 2)]
print(dictionary)
#Change the following list of lists to a list of concatenated strings:

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
conc = [x for sub in names for sub2 in sub for x in sub2]
concatenate = [conc[i] + ' ' + conc[i + 1] for i in range(0, len(conc), 2)]
print(concatenate)
#Write a lambda function which can solve a slope or y-intercept of linear functions
slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
y_intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1
print(y_intercept)
