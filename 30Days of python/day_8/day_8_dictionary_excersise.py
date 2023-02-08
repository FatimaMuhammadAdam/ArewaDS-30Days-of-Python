#Create an empty dictionary called dog
dog ={}
#Add name, color, breed, legs, age to the dog dictionary
dog ={ 'name': 'faty_dog', 'color': 'black brown', 'legs': 4, 'age': '6 month'

}
#Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student_dictionary = {
    "first_name": "Fatima",
    "last_name": "Muhammad Adam",
    "gender": "Female",
    "age": 26,
    "marital_status": "single",
    "skills": ["python", "git", "c++"],
    "country": "Nigeria",
    "city": "Dutse",
    "address": "Dutse",
}
#Get the length of the student dictionary
print(len(student_dictionary))
#Get the value of skills and check the data type, it should be a list
print(student_dictionary["skills"])
print(type(student_dictionary["skills"]))
#Modify the skills values by adding one or two skills
student_dictionary["skills"].append("tailoring")
#Get the dictionary keys as a list
list_keys = (list(student_dictionary.keys()))
#Get the dictionary values as a list
values = (list(student_dictionary.values()))
#Change the dictionary to a list of tuples using items() method
print(student_dictionary.items())
#Delete one of the items in the dictionary
student_dictionary.pop("age")
#Delete one of the dictionaries

del dog 