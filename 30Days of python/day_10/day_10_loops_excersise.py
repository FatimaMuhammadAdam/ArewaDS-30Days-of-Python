#Exercises: Level 1
import sys

sys.path.append('data')
# noinspection PyUnresolvedReferences
import countries
# noinspection PyUnresolvedReferences
import countries_data
#Iterate 0 to 10 using for loop, do the same using while loop.

for b in range(0,11):
    print(b)
    b = 0
while b <=10:
    print(b)
    b += 1
#Iterate 10 to 0 using for loop, do the same using while loop
for y in range(11,-1, -1):
    print(y)

    y = 10
while y >=0:
    print (y)
    y -=1
#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
string_hash = '#'
for v in range(1, 10):
    print("#" *v)

#Use nested loops to create the following:
for o in (1, 9):
    for t in (1, 9):
        print('#', end = '')
    print( )
#Print the following pattern:

"""0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100"""
for z in range( 1, 11 ):
  print(z,'x', z, '=', z*z)
#Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
items = ['Python', 'Numpy','Pandas','Django', 'Flask'] 
for y in items:
    print(y)

#Use for loop to iterate from 0 to 100 and print only even numbers
for h in range(0,100):
    if h % 2 == 0:
       print(h)
       h ++ 2
#Use for loop to iterate from 0 to 100 and print only odd numbers
for d in range (0, 100):
    if d % 2 == 1:
        print(d)
        d ++ 2
#Exercises: Level 2
#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum_num =0
for r in range(0,101):
    sum_num += r
print("the sum of all number:", sum_num)

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even_num = 0
old_num = 0
for c in range(0,100):
    if c % 2 == 0:
      even_num += c
    else:
      old_num += c
print("the sum of all old numbers", even_num)
print("the sum of all old numbers", old_num)
#Exercises: level 3
# Loop through the countries and extract all the countries containing the word land.

list_c = countries.country_list
for country in list_c:
    if "land" in country:
        print(country)
#This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruity_list = ['banana', 'orange', 'mango', 'lemon']
rev = []
for i in range(3, -1, -1):
    rev.append(fruity_list[i])
print(rev)
#

# 3
# noinspection DuplicatedCode
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
for i in list(counts.items())[:10]:
    print(i)
populations = {}
for i in list_data:
    populations[i["name"]] = i["population"]
populations = sort_dict_by_value(populations, True)
for i in list(populations.items())[:10]:
    print(i)
