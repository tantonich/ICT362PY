# def greet_user():
# 	"""Display a simple greeting."""
# 	print("Hello!")
# greet_user()

# def greet_user(username):
# 	"""Display a simple greeting."""
# 	print("Hello, " + username.title() + "!")
# greet_user('taylor')

# 8-1 Display Message
# def display_message():
# 	"""Display the chapter information"""
# 	print("We are learning about functions in chapter 8!")
# display_message()

# 8-2 Favorite Book
# def favorite_book(title):
# 	print("One of my favorite books is " + title.title() + "!")
# favorite_book("alice in wonderland")

# def describe_pet(animal_type, pet_name):
# 	"""Display information about a pet."""
# 	print("\nI have a " + animal_type + ".")
# 	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet('hamster', 'harry')
# describe_pet(animal_type='dog', pet_name='willie')

# def describe_pet(pet_name, animal_type='dog'):
# 	"""Display information about a pet."""
# 	print("\nI have a " + animal_type + ".")
# 	print("My " + animal_type + "'s name is " + pet_name.title() + ".")
# describe_pet('hamster', 'harry')
# describe_pet(animal_type='dog', pet_name='willie')
# describe_pet(pet_name='willie')
# describe_pet('willie')

# 8-3 T-Shirt
def make_shirt(size, text):
	"""Size and text to display on a shirt"""
	print("\nThe shirt size is " + size + " and the text will be \"" + text + "\".")
# make_shirt('small', 'hippos')
# make_shirt(size='medium', text='Yeah science!')

# 8-4 Large Shirts
def make_shirt(text='I love Python', size='Large'):
	"""Size and text to display on a shirt"""
	print("\nThe shirt size is " + size + " and the text will be \"" + text + "\".")
# make_shirt()
# make_shirt(size='medium')
# make_shirt('This is what I wear', 'Extra-large')

# 8-5 Cities
def describe_city(city, country='australia'):
	print(city.title() + " is in " + country.title())
# describe_city('sydney')
# describe_city(city='perth')
# describe_city('denver', 'united states')

def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + ' ' + last_name
	return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

def get_formatted_name(first_name, last_name, middle_name=''):
	"""Return a full name, neatly formatted."""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()
musician = get_formatted_name('john', 'hooker')
# print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

def build_person(first_name, last_name):
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	return person
musician = build_person('jimi', 'hendrix')
# print(musician)

def build_person(first_name, last_name, age=''):
	"""Return a dictionary of information about a person."""
	person = {'first': first_name, 'last': last_name}
	if age:
		person['age'] = age
	return person
musician = build_person('jimi', 'hendrix', age=27)
# print(musician)

# def get_formatted_name(first_name, last_name):
# 	"""Return a full name, neatly formatted."""
# 	full_name = first_name + ' ' + last_name
# 	return full_name.title()
# while True:
# 	print("\nPlease tell me your name:")
# 	print("(Enter 'q' at any time to quit)")
# 	f_name = input("First name: ")
# 	if f_name == 'q':
# 		break
# 	l_name = input("Last name: ")
# 	if l_name == 'q':
# 		break
# 	formatted_name = get_formatted_name(f_name, l_name)
# 	print("\nHello, " + formatted_name + "!")

# 8-6 City Names
def city_country(city, country):
	place = city.title() + ', ' + country.title()
	return place
city_name = city_country('frankfurt', 'germany')
# print(city_name)

# 8-7 Album using dictionary
def make_album(artist, album, tracks = ''):
	record = {'artist_name': artist, 'album_name': album}
	if tracks:
		record['tracks'] = tracks
	return record
# new_record = make_album('JayZ', 'Greatest Hits')
# print(new_record)
# new_record2 = make_album('Rihanna', 'One Hit Wonder')
# print(new_record2)
# new_record3 = make_album('Eminem', 'Slim Shady', '11')
# print(new_record3)

# 8-8 User Albums
# def make_album(artist, album, tracks = ''):
# 	record = {'artist_name': artist, 'album_name': album}
# 	if tracks:
# 		record['tracks'] = tracks
# 	return record

# while True:
# 	print("\nEnter the album information")
# 	print("(Enter 'q' at any time to quit)")

# 	i_artist = input("Artist name: ")
# 	if i_artist == 'q':
# 		break
# 	i_album = input("Album name: ")
# 	if i_album == 'q':
# 		break
# 	new_record = make_album(i_artist, i_album)
# 	print(new_record)

def greet_users(names):
	"""Print a simple greeting to each user in the list."""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)
usernames = ['hannah', 'ty', 'margot']
# greet_users(usernames)

def print_models(unprinted_designs, completed_models):
	"""
	Simulate printing each design, until none are left.
	Move each design to completed_models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		# Simulate creating a 3D print from the design.
		print("Printing model: " + current_design)
		completed_models.append(current_design)
def show_completed_models(completed_models):
	"""Show all the models that were printed."""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# print_models(unprinted_designs[:], completed_models)
# show_completed_models(completed_models)
# print(unprinted_designs)

def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile
user_profile = build_profile('albert', 'einstein',
	location='princeton',
	field='physics')
print(user_profile)