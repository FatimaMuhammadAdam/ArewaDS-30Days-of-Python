#Filter only negative and zero in the list using list comprehension
#numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
def filter_list():
    numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
    return [x for x in numbers if x<=0]

