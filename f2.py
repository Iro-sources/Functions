print("---------///////////DICTIONARIES/////------------")

person = {'f_name': 'eric',
          'l_name': 'django',
          'age': 56,
          }
city_value = person.get('city' 'no city is found')
print(person['f_name'])
print(person['l_name'])
print(person['age'])
print(city_value)

print("---------TRY IT YOURSELF 6.2------------")

favorite_numbers = {'sarah': 5,
                    'willie': 6,
                    'ever': 7,
                    'iona': 8}

numbers = favorite_numbers['sarah']
print(f"Sara's favorite number is: {numbers}")

numbers = favorite_numbers['willie']
print(f"willie's favorite number is: {numbers}")

numbers = favorite_numbers['ever']
print(f"ever's favorite number is: {numbers}")

numbers = favorite_numbers['iona']
print(f"Ionas favorite number is: {numbers}")

print("---------TRY IT YOURSELF 6.3------------")

glossary = {'pop': 'waxay tirtaa erayga ugu dambeeya listga',
            'append': 'gadaal ayay listga wax uga dartaa',
            'remove': 'waxay tirta oo kaliya markii la yaqaano magaca valuega aad tiraysid',
            'del': 'waxaa la isticmaala marki aad taqaanid positionka valuega aad tiraysid',
            'sorted': 'permanent',
            'sort': 'temporary'}
# word = 'pop'
# print(f"{word.title()}: {glossary[word]}")
word = glossary['pop'].title()
print(f"Pop: {word}.")

word = glossary['append'].title()
print(f"Append: {word}.")

word = glossary['remove'].title()
print(f"Remove: {word}.")

word = glossary['del'].title()
print(f"Del: {word}.")

word = glossary['sorted'].title()
print(f"Sorted: {word}.")

word = glossary['sort'].title()
print(f"Sort: {word}.")

print("---------TRY IT YOURSELF 6.4------------")

glossary = {'pop': 'waxay tirtaa erayga ugu dambeeya listga',
            'append': 'gadaal ayay listga wax uga dartaa',
            'remove': 'waxay tirta oo kaliya markii la yaqaano magaca valuega aad tiraysid',
            'del': 'waxaa la isticmaala marki aad taqaanid positionka valuega aad tiraysid',
            'sorted': 'permanent',
            'sort': 'temporary'}
print("Ku waan waxaa looqoray alphabetical order")
for word, vocabulary in sorted(glossary.items()):
    print(f"{word}: {vocabulary}.")

# for word in glossary.keys():
#     print(word)

#Habkaan waa sida defaultga ah ee dictionary lagu loopgareeyo
#Wuxuu kuu daabacaa oo kaliya Keyska dictionaryga
for word in glossary:
    print(word)

print()
for vocabulary in set(glossary.values()):
    print(vocabulary)

print("---------TRY IT YOURSELF 6.5------------")

rivers = {'nile': 'egypt',
          'mississippi': 'usa',
          'shabeele': 'somalia'
          }

for wabi, wadan in rivers.items():
    print(f"{wabi.title()}, runs through {wadan.title()}.")

print("---------TRY IT YOURSELF 6.6------------")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['jen', 'mohamed', 'sarah', 'ihsan', 'edward', 'ridwan', 'phil']

for name in friends:
    if name in favorite_languages:
        print(f"{name}, thanks for taking this poll!")
    else:
        print(f"{name}, can you share with us your favorite language?")

print("---------TRY IT YOURSELF 6.7------------")

people = []

person = {'f_name': 'eric',
          'l_name': 'django',
            'city': 'colorado',
          'age': 56}
people.append(person)

person = {'f_name': 'sarah',
          'l_name': 'diaku',
            'city': 'tehran',
          'age': 43}
people.append(person)

person = {'f_name': 'mohamed',
          'l_name': 'iro',
          'city': 'mogadishu',
          'age': 33}
people.append(person)
#to print all the information in a list of dictionaries you use a forloop as usual
for person in people:
    name = f"{person['f_name'].title()} {person['l_name'].title()}"
    city = person['city']
    age = person['age']
    print(f"{name} is from {city} and is {age} years old.")

print("---------TRY IT YOURSELF 6.8------------")
# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal type': 'python',
    'name': 'john',
    'owner': 'guido',
    'weight': 43,
    'eats': 'bugs',
}
pets.append(pet)

pet = {
    'animal type': 'chicken',
    'name': 'clarence',
    'owner': 'tiffany',
    'weight': 2,
    'eats': 'seeds',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'peso',
    'owner': 'eric',
    'weight': 37,
    'eats': 'shoes',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

print("---------TRY IT YOURSELF 6.9------------")

favorite_places = {'asluub': ['bandiradley'],
                    'clarence': ['newyork', 'tokyo'],
                   'tiffany': ['chicago', 'losangeles', 'lasvegas']
                   }
#First looping through the dictionary
for name, places in favorite_places.items():
    print(f"Here are {name}'s favorite places")
    #Second looping through the list inside the dictionary
    for place in places:
        print(place.title())

print("---------TRY IT YOURSELF 6.10------------")

favorite_numbers = {
                    'sarah': [5, 4, 3],
                    'willie': [6, 2, 1],
                    'ever': [7, 0, 12],
                    'iona': [8, 13, 20]
}
#First looping through the dictionary
for name, numbers in favorite_numbers.items():
    print(f"Here are {name}'s favorite numbers:")
    #Second looping through the list inside the dictionary
    for number in numbers:
        print(number)

print("---------TRY IT YOURSELF 6.11------------")

cities = {
    'oslo':  {'country': 'norway',
              'population': 697010,
'fact': 'a cool city'},

'lagos': {'country': 'nigeria',
          'population': 14368000,
          'fact': 'the most polulated city in africa'},

'istanbul': {'country': 'turkey',
            'population': 15415197,
            'fact': 'the best city for tourists'}
}

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact']

    # print(f"\n{city.title()} is in {country}.")
    # print(f"  It has a population of about {population}.")
    # print(f"  The {fact} mounats are nearby.")

    print(f"\n{city.title()} is in {country} which has a population of {population}, and is {fact}")




