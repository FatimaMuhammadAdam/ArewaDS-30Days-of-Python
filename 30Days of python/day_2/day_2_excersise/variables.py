#Day 2: 30 Days of python programming
firstname = 'FATIMA'
lastname = 'MUHAMMMAD ADAM'
full_name = firstname, lastname
country = 'Nigeria'
city = 'Dutse'
age =27
year = 2023
is_married = 'not married'
is_true = 3.5
is_light = 'paper'
name_bf, name_gf ='adamu','aisha'
print(name_bf,name_gf)
#Exercises: Level 2
print(type(firstname ))
print(type(lastname))
print(type(country))
print(type(age))
print(type(is_true))
print(type(year))
print(len(firstname),lastname)
num_one = 5
num_two = 4
total = num_one + num_two
print(total)
x = num_two -num_one
x
y = num_one/num_two
y
z =num_two * num_one
z
p =num_one%num_one
p
u = num_one**num_two
u
f = num_one//num_two
#question 5
import math

radius = 30

area_of_circle = math.pi * (radius ** 2)
circum_of_circle = 2 * math.pi * radius

print("Area of Circle:", area_of_circle)
print("Circumference of Circle:", circum_of_circle)
radius =float( input('enter the your radious sizes'))
print("Area of Circle: {:.2f} square meters".format(area_of_circle))
#question 6
firstname = input('what is your firstname?')
lastname = input('what is your name?')
country = input('please from which country are you from?')
age = input('please enter your age')
#question 7
help('keywords')

