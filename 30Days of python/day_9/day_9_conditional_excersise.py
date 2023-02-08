#Exercises: Level 1
#Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
age = int(input("please enter your age:"))
if age >= 18:
  print("congratulation you're old enough to drive in any part in nigeria")
else:
  print("please wait for", 18 -age, "missing amount of years you can't drive now in any part of nigeria")
#Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = 27
your_age = int(input("please enter your age:"))
if my_age == your_age:
    print("Thank God we're at the same age" )  
    
elif your_age >my_age:
    print("O no! you're", your_age - my_age, "older than me")
else:
    print('Heheeeh! I am older than you')
 
#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b
a = int(input('enter the first number:'))
b = int(input('enter the second number:'))
if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is lesser than", b)
else:
    print("Both numbers are equal")
### Exercises: Level 2
#Write a code which gives grade to students according to theirs scores:
grade_score = int(input("please enter the student grades"))

grades = {}
for i in range(90, 101):
    grades[i] = 'A'
for i in range(70, 90):
    grades[i] = 'B'
for i in range(60, 70):
    grades[i] = 'C'
for i in range(50, 60):
    grades[i] = 'D'
for i in range(0, 50):
    grades[i] = 'F'
print("the student grade score is:", grades[(grade_score)])
#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input ("enter then month").title()
for i in month["September", "October", "November"]:
    print("the season is Autumn")
for i in month["December", "January", "February"]:
    print ("the season is Winter")
for i in month["March", "April", "May"]:
   print(" the season is spring ")
for i in month ["June", "July", "August"]:
   print(" the season is summer")
#The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit = input("please enter the name of the fruits")
print("the fruit you enter is in the fruits container" if fruit in fruits else fruits.apppend())
print(fruits)


#Exercises: Level 3
#Here we have a person dictionary. Feel free to modify it!

person={
    'first_name': 'Fatin Baba',
    'last_name': 'Muhammad Babura ',
    'age': 27,
    'country': 'Nigeria',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'saloon','Python','Makeup', 'taloring', 'fashion design'],
    'address': {
        'street': 'Space street',
        'zipcode': '721011'
    }
    }
#Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if person['skills']:
    print(person['skills'][len(person['skills'])//2])
 #Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
    print ("Pyhton" in person['skills'])  
#If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
if ["JavaScript", "React"] == person ["skills"]:
    print('she is a front end developer')
if [" Node", "Python", "MongoDB"] == person ["skills"]:
    print('she is a backend developer')
if ["React", "Node", "MongoDB"] == person["skills"]:
    print('she is a fullstack developer') 
if ['Makeup', 'taloring', 'fashion design'] == person['skills']:
    print('she is a women enterprenuer') 
else:
    print("unknown title")
#If the person is married and if he lives in Finland, print the information in the following format:
if person ['is_marred' ]:
    print(person['first_name'],person['last_name'],"lives in", person['country'], "she is married")
else:
    print(person['first_name'],person['last_name'],"lives in", person['country'], "she is not married")