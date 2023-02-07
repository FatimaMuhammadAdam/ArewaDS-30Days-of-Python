#day four execersise 
# 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
print('Thirty' + ' Days' + ' Of' + ' Python')

# 2Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
print(' '.join(['Coding', 'For', 'All']))

# 3 Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Coding For All'

# 4 Print the variable company using print().
print(company)

# 5 Print the length of the company string using len() method and print().
print(len(company))

# 6 Change all the characters to uppercase letters using upper() method.
print(company.upper())

# 7 Change all the characters to lowercase letters using lower() method.
print(company.lower())

# 8Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9 Cut(slice) out the first word of Coding For All string.
print(company[7:])
# 10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company[company.index('Coding'):8])
print(company[company.find('Coding'):8])

# 11 Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding ', 'Not '))

# 12Change Python for Everyone to Python for All using the replace method or other methods
print('Python For Everyone'.replace('Everyone', 'All'))

# 13 Split the string 'Coding For All' using space as the separator (split()) .
print(company.split())

# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(','))

# 15 What is the character at index 0 in the string Coding For All.
print(company[0])

# 16 What is the last index of the string Coding For All
print(len(company) - 1)

# 17 What character is at index 10 in "Coding For All" string.
print(company[10])

# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
words = "Python For Everyone".split()
print(words[0][0] + words[1][0] + words[2][0])

# 19 Create an acronym or an abbreviation for the name 'Coding For All'.
words = 'Coding For All'.split()
print(words[0][0] + words[1][0] + words[2][0])

# 20
print("Coding For All".index('C'))
# 21
print("Coding For All".index('F'))

# 22
print("Coding For All People".rfind('l'))

# 23
print('You cannot end a sentence with because because because is a conjunction'.find('because'))

# 24
print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))

# 25
print('You cannot end a sentence with because because because is a conjunction'.replace('because because because', ''))

# 26
print('You cannot end a sentence with because because because is a conjunction'.find('because'))

# 27
print('You cannot end a sentence with because because because is a conjunction'.replace('because because because', ''))

# 28
print('Coding For All'.startswith('Coding'))

# 29
print('Coding For All'.endswith('coding'))

# 30
print('   Coding For All      '.rstrip().lstrip())

# 31
print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

# 32
print('-'.join(['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']))

# 33
print('I am enjoying this challenge.\nI just wonder what is next.')

# 34
print('Name\tAge\tCountry\tCity\nRishabh\t250\tFinland\tHelsinki')

# 35
print('radius =', 10)
print('area =', 3.14, '* radius **', 2)
print('The area of a circle with radius', 10, 'is', 314, 'meters square.')

# 36
print('8 + 6 = 14')
print('8 - 6 = 2')
print('8 * 6 = 48\n8 / 6 = 1.33\n8 % 6 = 2\n8 // 6 = 1\n8 ** 6 = 262144')