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
