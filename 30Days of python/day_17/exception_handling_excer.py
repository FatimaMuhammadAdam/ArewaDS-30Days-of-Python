
#Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
#first way
*nordic_countries, es, ru = names
print(nordic_countries, es, ru)
#second way with exception 
try:
    *nordic_countries, es, ru = names
    print(nordic_countries, es, ru)
except Exception as d:
    print(d)

