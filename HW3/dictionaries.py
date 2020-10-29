favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }
# print("Sarah's favorite language is " + 
#     favorite_languages['sarah'].title() + 
#     ".")
# for name, language in favorite_languages.items():
#     print(name.title()+"'s favorite language is "+language.title()+".")

# 6-1 Person
friend = {
    'first_name':'gerald',
    'last_name':'bradley',
    'city':'rio rancho',
    }
# print(friend['first_name'].title())
# print(friend['last_name'].title())
# print(friend['city'].title())

# 6-2 Favorite numbers
favorite_numbers = {
    'jenny':'2',
    'tyler':'1',
    'scott':'4',
    'krista':'34',
    'alex':'7',
    }
# for key in favorite_numbers:
#     print(key.title()+"'s favorite number is "+favorite_numbers[key])
# print("Jenny's favorite number is "+favorite_numbers['jenny']+".\n"+
#     "Tyler's favorite number is "+favorite_numbers['tyler']+".\n"+
#     "Scott's favorite number is "+favorite_numbers['scott']+".\n"+
#     "Krista's favorite number is "+favorite_numbers['krista']+".\n"+
#     "Alex's favorite number is "+favorite_numbers['alex']+".\n")

# 6-3 Glossary
glossary = {
    'variable':'A Python variable is a reserved memory location to store values.',
    'list':'The list is a most versatile datatype available in Python which can be written as a list of comma-separated values (items) between square brackets.',
    'tuple':'A datatype that can\'t be overwritten.',
    }
# for key in glossary:
#     print(key.title()+": "+glossary[key])

# for loops with dictionaries
user_0 = {
    'username':'efermi',
    'first':'enrico',
    'last':'fermi',
    }

# for key, value in user_0.items():
#     print("\nKey: " + key)
#     print("Value: " + value)
# for key in user_0:
#     print("\nKey: " + key)
#     print("Value: " + user_0[key])

# keys method
# Looping through keys in a dictionary
# for name in favorite_languages.keys():
#     print(name.title())

# for name in favorite_languages:
#     print(name.title())

friends = ['phil', 'sarah']
# for name in favorite_languages.keys():
#     print(name.title())

#     if name in friends:
#         print(" Hi " + name.title() +
#             ", I see your favorite language is " + 
#             favorite_languages[name].title() + "!")

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# Sorting a dictionary and looping
# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")

# values method
# print("The following languages have been mentioned:")
# for language in favorite_languages.values():
#     print(language.title())

# set() to remove duplicates
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

# 6-4 Glossary 2
# for word, definition in glossary.items():
#     print(word.title() + ": " + definition.title())

# 6-5 Rivers
rivers = {
    'rio grande':'new mexico',
    'animas river':'colorado',
    'gila river':'arizona',
    }
# for river, state in rivers.items():
#     print("The "+river.title()+" runs through "+state.title()+".")
# for river in rivers.keys():
#     print(river.title())
# for state in rivers.values():
#     print(state.title())

# 6-6 Polling
participants = ['jen', 'steve', 'alex', 'chris', 'sarah']
for participant in sorted(participants):
    if participant not in favorite_languages:
        print(participant.title() + ", pleae participate in the poll.")

    if participant in favorite_languages:
        print(participant.title()+", thank you for taking the poll.")