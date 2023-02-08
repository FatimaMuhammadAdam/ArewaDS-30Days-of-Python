# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#Exercises: Level 1

#Find the length of the set it_companies
print(len(it_companies))
#Add 'Twitter' to it_companies
it_companies.add('Twitter')
#Insert multiple IT companies at once to the set it_companies
it_companies.update(['HP','Dell', 'telegram', 'tiktok'])
it_companies
#Remove one of the companies from the set it_companies
it_companies.remove("HP")
#What is the difference between remove and discard
""" remove() method  raise errors.on the other hand discard() method doesn't raise any errors."""

#Exercises: Level 2
#Join A and B
print(A.union(B))
#Find A intersection B
print(A.intersection(B))
#Is A subset of B
print('is A subst of B:', A.issubset(B))
#Are A and B disjoint sets
print('There is no similarity between A and B',A.isdisjoint(B))
#Join A with B and B with A
print(A.union(B))
print(B.union(A))
#What is the symmetric difference between A and B
print(A.symmetric_difference(B))
#Delete the sets completely
del A
del B

#Exercises: Level 3
#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(len(set(age)) < len(age))  # len of list is bigger
#Explain the difference between the following data types: string, list, tuple and set
"""
String : is  any set of alphaset, numeric etc  surrounded by either single quotation marks, or double quotation marks.
list: used to store multiple items in a single variable, Lists are created using square brackets
tuple:  is a collection which is ordered and unchangeable.
set: is a collection of unordered and un-indexed distinct elements.
"""
#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
#set =(sentence)
print(len(set(sentence.split())))