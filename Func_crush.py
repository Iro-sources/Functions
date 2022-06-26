#1
def greet_user():


    print("hello!")
greet_user()

#2
def greet_user(parameter):

    print(f"hello! {parameter}")


greet_user('ali')

#3
def greet_user(a, b):
    print(a, b)


greet_user(2, 4)

#4
def greet_user(a, b=5):
    print(a + b)


greet_user(2, 7)

#5
def names(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name
print(names('jimy', 'fox'))

#6
def multiple(c, d):

    return c * d
print(multiple(5, 8))

print("************************Oppgave 8.6************************")

def land(country, city):

    print(f"This is the country name {country.title()} and here is it's city {city.title()}")

def wadan():

    print("waxkale")

land('somalia', 'mogadishu')
land('norway', 'oslo')
wadan()
land('argentina', 'bonasaries')


def make_album(title, artist, tracks=0):
    """returns an album of songs and it's artists"""
    build_album = {'title': title.title(),
                   'artist': artist.title()
                   }
    if tracks:
        build_album['tracks'] = tracks
    return build_album


album = make_album('beethoven', 'ninth symphony')
print(album)

album = make_album('willie nelson', 'red-headed stranger')
print(album)

album = make_album('iron maiden', 'piece of mind', tracks=8)
print(album)



def make_album(title, artist, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'title': title.title(),
        'artist': artist.title(),
    }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break

    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(title, artist)
    print(album)

print("\nThanks for responding!")


class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

#Magic starts from here
    def set_number_served(self, number_served):
        self.number_served = number_served
        """Allow user to set the number of customers that have been served."""


    def increament_number_served(self, number_served):
        self.number_served += number_served

restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 23
print(f"\nNumber served: {restaurant.number_served}")

restaurant.set_number_served(5252)
print(f"\nNumber served: {restaurant.number_served}")

restaurant.increament_number_served(8989)
print(f"\nNumber served: {restaurant.number_served}")

for index in range(len(filmer)):
    for key in filmer[index]:
        print(filmer[index][key])



dataList = [{'a': 1}, {'b': 3}, {'c': 5}]
for dic in dataList:
    for key in dic:
        print(dic[key])