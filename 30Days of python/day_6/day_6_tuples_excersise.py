#tuples 
#Exercises: Level 1
#Create an empty tuple
fatima_muhammad_adam = ()
#Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
mysis_siblings =('aisha','zee', 'hajara')
mybros_siblings = ('khalifa', 'abubakar')
#Join brothers and sisters tuples and assign it to siblings
siblings = mysis_siblings + mybros_siblings
#How many siblings do you have?
print(len(siblings))
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ("father", "mother")
#Exercises: Level 2
#Unpack siblings and parents from family_members
*siblings, mother, father = family_members
print(siblings)
print(father)
print(mother)
#Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('orange','gauva','water lemon')
vegetables = ('ogun leaf', 'latos','cabbage')
animal_products = ('manure','milk')
food_stuff_tp = fruits + vegetables + animal_products

#Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
food_stuff_lt = food_stuff_lt[:len(food_stuff_lt) // 2] + food_stuff_lt[len(food_stuff_lt) // 2 + 1:]
food_stuff_tp = tuple(food_stuff_lt)

#Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[len(food_stuff_lt) - 3:]
print(food_stuff_lt)
print(first_three)
print(last_three)

#Delete the food_staff_tp tuple completely
del food_stuff_tp
#Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)