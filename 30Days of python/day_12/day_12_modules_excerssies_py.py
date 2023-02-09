
#day 12 importing modules and creating them
#Exercises: Level 1
#Writ a function which generates a six digit/character random_user_id.
"""  print(random_user_id());
  '1ee33d'
"""
#

import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890'
char_list = []
char_list[:0] = chars


# Level 1

def random_user_id():
    identity = ''
    for _ in range(6):
        identity += random.choice(char_list)
    return identity

#Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
"""print(user_id_gen_by_user()) # user input: 5 5
#output:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr"""


def user_id_gen_by_user():
    charsize = int(input('Enter Character Size: '))
    charlimit = int(input('Enter how many user ids to generate: '))
    for _ in range(charlimit):
        identity = ''.join([random.choice(char_list) for _ in range(charsize)])
        print(identity)

#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    r = str(random.randint(0, 255))
    g = str(random.randint(0, 255))
    b = str(random.randint(0, 255))
    return "rgb(" + r + "," + g + "," + b + ")"


# Level 2
#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #.
#Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

def list_of_hexa_colors(many=0):
    if many == 0:
        many = random.randint(1, 10)
    hexas = "1,2,3,4,5,6,7,8,9,0,a,b,c,d,e,f".split(",")
    hexCodes = []
    for _ in range(many):
        hexCodes.append("#" + ''.join([random.choice(hexas) for _ in range(6)]))
    return hexCodes

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(many=0):
    if many == 0:
        many = random.randint(1, 10)
    rgbs = []
    for _ in range(many):
        rgbs.append(rgb_color_gen())
    return rgbs

#Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(type_of_col, many):
    if type_of_col == 'hexa':
        return list_of_hexa_colors(many)
    elif type_of_col == 'rgb':
        return list_of_rgb_colors(many)
    else:
        return "Invalid Input"


# Level 3
#Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffled_list(array):
    return random.sample(array, len(array))

#Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def seven_random():
    arr = []
    length = -1
    while length <= 7:
        num = random.randint(0, 9)
        if num not in arr:
            arr.append(num)
            length = len(arr)
    return arr

