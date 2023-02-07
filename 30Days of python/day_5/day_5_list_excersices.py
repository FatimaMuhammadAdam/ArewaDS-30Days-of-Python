#Exercises: Level 1
#1 Declare an empty list
fati_list = list()
#2 Declare a list with more than 5 items
fati_more_than_5 = [1, 2, 3, 4, 5, 6]
#3 Find the length of your list
print(len(fati_more_than_5))
#4 Get the first item, the middle item and the last item of the list
print(fati_more_than_5[0], fati_more_than_5[len(fati_more_than_5) // 2], fati_more_than_5[-1])
# 5Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_list = ['fatima',25, 57, 'single', 'Dutse']

# 6 Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
#7 Print the list using print()
print(it_companies)

#8 Print the number of companies in the list
print(len(it_companies))
#9 Print the first, middle and last company
print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1])
# 10  the list after modifying one of the companies
it_companies[0] = 'Infosys'
print(it_companies)
# 11 Add an IT company to it_companies
it_companies.append('Facebook')
#12 Insert an IT company in the middle of the companies list
it_companies = it_companies[0:len(it_companies) // 2] + ['Dell'] + it_companies[len(it_companies) // 2:]
# 13 Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[0] = it_companies[0].upper()
#14 Join the it_companies with a string '#;  '
it_companies_hash = '#'.join(it_companies)
#15 Check if a certain company exists in the it_companies list.
print('IBM' in it_companies)
# 16 Sort the list using sort() method
it_companies.sort()
#17 Reverse the list in descending order using reverse() method
it_companies.reverse()
#Slice out the first 3 companies from the list
it_companies = it_companies[2:]

# 19 Slice out the last 3 companies from the list
it_companies = it_companies[:len(it_companies) - 3]

# 20 Slice out the middle IT company or companies from the list
it_companies = it_companies[0:len(it_companies) // 2] + it_companies[len(it_companies) // 2 + 1:]

# 21 Remove the first IT company from the list
it_companies.pop(0)

# 22 Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies) // 2)

# 23 Remove the last IT company from the list
it_companies.pop(len(it_companies) - 1)

# 24 Remove all IT companies from the list
it_companies.clear()

# 25 Destroy the IT companies lis
del it_companies

# 26 Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux'] 
back_end = ['Node','Express', 'MongoDB']
front_end.append(back_end)
#After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end
indx = full_stack.index('Redux')
full_stack = full_stack[:indx] + ['Python', 'SQL'] + full_stack[indx:]

#Exercises: Level 2
#1 The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
print(ages)
print(ages[0])
print(ages[-1])
#Add the min age and the max age again to the list
print('0.2f'.format((ages[len(ages)//2] + ages[~(len(ages)//2)])/2))
#Find the median age (one middle item or two middle items divided by two)
print('0.2f'.format(sum(ages) / len(ages)))
#Find the average age (sum of all items divided by their number )
print(ages[-1] - ages[0])
#Find the range of the ages (max minus min)
print(abs(ages[0] - sum(ages) / len(ages)))
#Compare the value of (min - average) and (max - average), use abs() method

print(abs(ages[-1] - sum(ages) / len(ages)))
#
countries = [
    'Afghanistan',
    'Albania',
    'Algeria',
    'Andorra',
    'Angola',
    'Antigua and Barbuda',
    'Argentina',
    'Armenia',
    'Australia',
    'Austria',
    'Azerbaijan',
    'Bahamas',
    'Bahrain',
    'Bangladesh',
    'Barbados',
    'Belarus',
    'Belgium',
    'Belize',
    'Benin',
    'Bhutan',
    'Bolivia',
    'Bosnia and Herzegovina',
    'Botswana',
    'Brazil',
    'Brunei',
    'Bulgaria',
    'Burkina Faso',
    'Burundi',
    'Cambodia',
    'Cameroon',
    'Canada',
    'Cape Verde',
    'Central African Republic',
    'Chad',
    'Chile',
    'China',
    'Colombia',
    'Comoros',
    'Congo (Brazzaville)',
    'Congo',
    'Costa Rica',
    "Cote d'Ivoire",
    'Croatia',
    'Cuba',
    'Cyprus',
    'Czech Republic',
    'Denmark',
    'Djibouti',
    'Dominica',
    'Dominican Republic',
    'East Timor (Timor Timur)',
    'Ecuador',
    'Egypt',
    'El Salvador',
    'Equatorial Guinea',
    'Eritrea',
    'Estonia',
    'Ethiopia',
    'Fiji',
    'Finland',
    'France',
    'Gabon',
    'Gambia, The',
    'Georgia',
    'Germany',
    'Ghana',
    'Greece',
    'Grenada',
    'Guatemala',
    'Guinea',
    'Guinea-Bissau',
    'Guyana',
    'Haiti',
    'Honduras',
    'Hungary',
    'Iceland',
    'India',
    'Indonesia',
    'Iran',
    'Iraq',
    'Ireland',
    'Israel',
    'Italy',
    'Jamaica',
    'Japan',
    'Jordan',
    'Kazakhstan',
    'Kenya',
    'Kiribati',
    'Korea, North',
    'Korea, South',
    'Kuwait',
    'Kyrgyzstan',
    'Laos',
    'Latvia',
    'Lebanon',
    'Lesotho',
    'Liberia',
    'Libya',
    'Liechtenstein',
    'Lithuania',
    'Luxembourg',
    'Macedonia',
    'Madagascar',
    'Malawi',
    'Malaysia',
    'Maldives',
    'Mali',
    'Malta',
    'Marshall Islands',
    'Mauritania',
    'Mauritius',
    'Mexico',
    'Micronesia',
    'Moldova',
    'Monaco',
    'Mongolia',
    'Morocco',
    'Mozambique',
    'Myanmar',
    'Namibia',
    'Nauru',
    'Nepal',
    'Netherlands',
    'New Zealand',
    'Nicaragua',
    'Niger',
    'Nigeria',
    'Norway',
    'Oman',
    'Pakistan',
    'Palau',
    'Panama',
    'Papua New Guinea',
    'Paraguay',
    'Peru',
    'Philippines',
    'Poland',
    'Portugal',
    'Qatar',
    'Romania',
    'Russia',
    'Rwanda',
    'Saint Kitts and Nevis',
    'Saint Lucia',
    'Saint Vincent',
    'Samoa',
    'San Marino',
    'Sao Tome and Principe',
    'Saudi Arabia',
    'Senegal',
    'Serbia and Montenegro',
    'Seychelles',
    'Sierra Leone',
    'Singapore',
    'Slovakia',
    'Slovenia',
    'Solomon Islands',
    'Somalia',
    'South Africa',
    'Spain',
    'Sri Lanka',
    'Sudan',
    'Suriname',
    'Swaziland',
    'Sweden',
    'Switzerland',
    'Syria',
    'Taiwan',
    'Tajikistan',
    'Tanzania',
    'Thailand',
    'Togo',
    'Tonga',
    'Trinidad and Tobago',
    'Tunisia',
    'Turkey',
    'Turkmenistan',
    'Tuvalu',
    'Uganda',
    'Ukraine',
    'United Arab Emirates',
    'United Kingdom',
    'United States',
    'Uruguay',
    'Uzbekistan',
    'Vanuatu',
    'Vatican City',
    'Venezuela',
    'Vietnam',
    'Yemen',
    'Zambia',
    'Zimbabwe',
]

# middle of the countries
print([countries[i]
       for i in range((len(countries) // 2) - (1 if int(len(countries)) % 2 == 0 else 0), len(countries) // 2 + 1)])

length = len(countries)
if length % 2 == 0:
    first_half = countries[:length // 2]
    second_half = countries[length // 2:]
else:
    first_half = countries[:length // 2 + 1]
    second_half = countries[length // 2 + 1:]
#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'][3:]