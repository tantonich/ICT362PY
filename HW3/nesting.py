## List of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

## Make an empty list for storing aliens.
aliens = []

## Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

## Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("...")

## Show how many aliens have been created.
print("Total number of aliens: " + str(len(aliens)))

## Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

## Summarize the order.
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print("\n" + name.title() + "'s favorite language is:")
        for language in languages:
            print("\t" + language.title())
    else:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())

## Dictionaries nested inside of Dictionaries
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
for username, user_info in users.items():
    print("\nUsername: " + username)

    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

## 6-7 People
friend_0 = {
    'first_name':'gerald',
    'last_name':'bradley',
    'city':'rio rancho',
    }
friend_1 = {
    'first_name':'jared',
    'last_name':'mcgaughey',
    'city':'rio rancho',
    }
friend_2 = {
    'first_name':'jerry',
    'last_name':'bruce',
    'city':'albuquerque',
    }
people = [friend_0, friend_1, friend_2]
for friend in people:
    print("My friend "+friend['first_name'].title()+" "+friend['last_name'].title()+
        " lives in " + friend['city'].title())

## 6-8 Pets
fuzzy = {
    'type':'cat',
    'owner':'sally',
    }
spot = {
    'type':'dog',
    'owner':'steve',
    }
porky = {
    'type':'pig',
    'owner':'greg',
    }
pets = [fuzzy, spot, porky]
for pet in pets:
    print(pet)

## 6-9 Favorite places
favorite_places = {
    'gerald':['kansas', 'texas', 'new orleans'],
    'jerry':['colorado', 'arizona', 'utah'],
    'jared':['la tierra', 'oak flats', 'placitas'],
    }
for friend, places in sorted(favorite_places.items()):
    print("\n"+friend.title()+"'s favorite places are:")
    for place in places:
        print("\t"+place.title())

# 6-10 Favorite numbers
favorite_numbers = {
    'jenny':['2', '30'],
    'tyler':['1', '16', '17'],
    'scott':['4', '11', '32'],
    'krista':['34', '22'],
    'alex':['7', '77', '777'],
    }
for gambler, numbers in favorite_numbers.items():
    print(gambler.title()+"'s favorite numbers are:")
    for number in numbers:
        print("\t"+number)

# 6-11 Cities
cities = {
    'albuquerque' : {
        'state':'new mexico',
        'population':'1 million',
        'fact':'has good food',
        },
    'denver' : {
        'state':'colorado',
        'population':'4 million',
        'fact':'has too much traffic'
        },
    'bozeman' : {
        'state':'montana',
        'population':'40 thousand',
        'fact':'has fun things to do outdoors'
        },
    }

cities['los angles'] = {'state':'california', 'population':'5 million',
    'fact':'has a lot of homeless people'}

for city, city_info in cities.items():
    print("\nCity: " + city.title())
    state = city_info['state']
    population = city_info['population']
    fact = city_info['fact']
    print("\tState: " + state.title())
    print("\tPopulation: " + population + " people")
    print("\tDid you know that "+city.title()+" "+fact+"?")
