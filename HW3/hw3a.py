# Create a dictonary called glossary
glossary = {}

# Have the glossary include a list of five (5) programing words you have learned in chapters 4-6.
# Use these words as keys to your dictionary.
# Find the definition of these words and use them as the values to the keys.
glossary['variable'] = 'A reserved memory location to store values.'
glossary['list'] = 'A list of comma-separated values (items) between square brackets.'
glossary['tuple'] = 'A datatype that can\'t be overwritten.'
glossary['loop'] = 'A way for programmers to iterate over items in a dataset.'
glossary['slice'] = 'Used to specify a specific items in a list.'

# Using a loop, print each word and its meaning as neatly formatted output.
for word, definition in glossary.items():
	print(word.title() + " - " + definition)

# Create three dictionaries called person.
# Have each of the person dictionaries represent a different person.
# Each dictionary should store a person's information to include their:
#	first name, last name, age, city
person_0 = {
    'first_name':'jerry',
    'last_name':'seinfeld',
    'age':66,
    'city':'new york',
    }
person_1 = {
    'first_name':'kevin',
    'last_name':'mccallister',
    'age':8,
    'city':'chicago',
    }
person_2 = {
    'first_name':'bruce',
    'last_name':'banner',
    'age':35,
    'city':'dayton',
    }
# Use the append() method to store all three dictionaries in a list called people.
people = []
people.append(person_0)
people.append(person_1)
people.append(person_2)

# Use a loop to go through each item in the list of people.
# As you loop, print everything you have stored about each person in neatly formatted output.
for person in people:
    print(person['first_name'].title()+" "+person['last_name'].title()+
        " lives in " + person['city'].title() + " and is " + 
        str(person['age']) + " years old.")