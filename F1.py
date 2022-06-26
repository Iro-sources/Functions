import char as char


def greet_user():
    print("hello")


greet_user()


def greet_user(username):
    print(f"hello, {username}")


greet_user('Ali')

print("___________________________________________")

def define_partners(name, pairs_with):

    print(f"{name} is the wife of {pairs_with}.")


define_partners('fartun', 'maxamed')

print("///////////////////////////////////////////")



# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
# Fibonacci seq # 1 + 2 + 3 + ... + 100

def fib(n):

    
    a = 1
    b = 1

    print(a)
    print(b)

    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)


fib(11)
print("------------------------------")

# factorial(n) = 1 * 2 * 3 * 4... * n
# write a function that will accept n and will return factorial of it # 1 * 3 * 5 * 7 * ... * 99

def factorial(n):
    res = 1
    for i in range(1, n+1):
        res = res * i
    return res


print(factorial(5))

x = 99
y = 10

if x == 0:
    if y == 10:
        print("yes")
    elif x == 99:
        print("no")

# temp = "5 degrees"
# cel = 0
# fahr = float(temp)
# cel = (fahr - 32.0) * 5.0 / 9.0
# print(cel)

print("Hi")
print("""This 
is
not
a
great""")

print("spam " * 4)
print(3 * '7')

spam = 7
spam = spam + 0
print(spam)

eggs = str(spam) + "3"
print(eggs)
print(float(eggs))



num = 7
if num > 8:
   print("3")
if num < 0:
   print("5")
if num ==7:
   print("7")



x = 0
y = 10

if x == 0:
    print("Indentation is significant in python")
if y == 10:
    print("Indentation is significant in python")

a = 2
if a <= 2 :
    print("small")
if a >= 2 :
    print("Medium")
else:
    print("large")

# Create a "Code" Generator that takes text as input and replaces each letter with another letter, and outputs the "encoded" message.


Dinner_invitation = ['ali', 'ahmed', 'asad']

name = Dinner_invitation[0].title()
print(f" {name.title()}, you're invited for a dinner on friday night, please attend")

name = Dinner_invitation[1].title()
print(f" {name.title()}, you're invited for a dinner on friday night, please attend")

name = Dinner_invitation[2].title()
print(f"{name.title()}, you're invited for a dinner on friday night, please attend")
print()

print(f"{Dinner_invitation[1].title()} can't attend the dinner")

del Dinner_invitation[1]
Dinner_invitation.insert(1, 'abdi')
print(Dinner_invitation)

name = Dinner_invitation[0].title()
print(f" {name.title()}, you're invited for a dinner on friday night, please attend")

name = Dinner_invitation[1].title()
print(f" {name.title()}, you're invited for a dinner on friday night, please attend")

name = Dinner_invitation[2].title()
print(f"{name.title()}, you're invited for a dinner on friday night, please attend")

print("--------------------------------")

print("we found a bigger table therefore, we can invite more guests yeeey")

Dinner_invitation.insert(0, 'abdirashid')
Dinner_invitation.insert(2, 'ridwan')
Dinner_invitation.append('dahir')
print(Dinner_invitation)
print()

name = Dinner_invitation[0].title()
print(f" {name}, you're invited for a dinner on friday night, please attend")

name = Dinner_invitation[1].title()
print(f" {name}, you're invited for a dinner on friday night, please attend")

name = Dinner_invitation[2].title()
print(f"{name}, you're invited for a dinner on friday night, please attend")

name = Dinner_invitation[3].title()
print(f" {name}, you're invited for a dinner on friday night, please attend")

name = Dinner_invitation[4].title()
print(f" {name}, you're invited for a dinner on friday night, please attend")

name = Dinner_invitation[5]
print(f"{name}, you're invited for a dinner on friday night, please attend")

print("---------TRY IT YOURSELF 3.9------------")
print(len(Dinner_invitation))

print("Sorry, I can invite only two people at dinner coz of the quarantine rules")


name = Dinner_invitation.pop()
print(f"sorry, {name.title()} this is happened coz of coronavirus rules")

name = Dinner_invitation.pop()
print(f"sorry, {name.title()} this is happened coz of coronavirus rules")

name = Dinner_invitation.pop()
print(f"sorry, {name.title()} this is happened coz of coronavirus rules")

name = Dinner_invitation.pop()
print(f"sorry, {name.title()} this is happened coz of coronavirus rules")
print(Dinner_invitation)

name = Dinner_invitation[0].title()
print(f"{name}, please come to dinner")

name = Dinner_invitation[1].title()
print(f"{name}, please come to dinner")
del Dinner_invitation[0]
del Dinner_invitation[0]
print(Dinner_invitation)

print("---------TRY IT YOURSELF 3.8------------")

tour_places = ['mogadishu', 'istanbul', 'london', 'nairobi']
print("Here is the original list:")
print(tour_places)

print("\n Here is the sorted list:")
print(sorted(tour_places) )

print("\n Here is the original list:")
print(tour_places)

tour_places.reverse()
print(tour_places)

tour_places.reverse()
print(tour_places)

tour_places.sort()
print(tour_places)

tour_places.sort(reverse=True)
print(tour_places)

for places in tour_places:
    print(f"{places.upper()}, I think this is a nice place to visit")


print("---------TRY IT YOURSELF 4.1------------")
pizzas = ['pepporini', 'meet', 'chicken', 'mix']

for pizza in pizzas:
    if pizza == 'meet':
        print(f"I don't like {pizza.title()} pizza")
    elif pizza == 'chicken':
        print(f"I like best {pizza.title()} pizza")
    else:
        print(f"I like {pizza.title()} pizza")

print("All in all I like pizza")

print("---------------------------------")

for value in range(1, 21):
    print(value)

print("---------------------------------")

jibaar = []
for value in range(1, 6):
    jibaar.append(value ** 2)
print(jibaar)

jibaar = [value ** 2 for value in range(1, 6)]
print(jibaar)

numbers = list(range(6, 12, 2))
print(numbers)

my_numbers = [2, 4, 9, 0, 45, 78, 5]
print(min(my_numbers))
print(max(my_numbers))
print(sum(my_numbers))
print(len(my_numbers))

print("---------TRY IT YOURSELF 4.3------------")
numbers = list(range(1, 21))
for number in numbers:
    print(number)

odd_numbers = range(1, 20, 2)
for number in odd_numbers:
    print(number)


print("---------TRY IT YOURSELF 4.7------------")
threes = list(range(3, 31, 3))

for number in threes:
    print(number)


print("---------TRY IT YOURSELF 4.8------------")
cubes = []
for value in range(1, 11):
    cube = (value**3)
    cubes.append(cube)

print(cubes)


print("---------TRY IT YOURSELF 4.9------------")
cubes = [value**3 for value in range(1, 11)]
print(cubes)

print("---------LIST COMPREHENSIONS------------")

#when you have a variable of lists
tiro = [1, 2, 3, 4, 5]
jibaar = [tir * 2 for tir in tiro]
print(jibaar)

#when you're starting from an empty list
tiro = []
for x in range(1, 6):
    tir = (x * 2)
    tiro.append(tir)

print(tiro)

magac = 'maxamed'
x = [char.splitlines() for char in magac]
print(x)

# friends = ['ali', 'ahmed', 'asad']
# new_friends = [name[0].upper() for name in friends]
# print(name)

friends = ['ashley', 'matt', 'michael']

wax_kale = [x.title() for x in friends]
print(wax_kale)

cusayb = [friend[0].upper()+friend[1:] for friend in friends]
print(cusayb)

tiro = [1, 2, 3, 4, 5]
string_list = [str(x) + "HELLO" for x in tiro]
print(string_list)


print("---------TRY IT YOURSELF 4.10------------")

pizzas = ['pepporini', 'meet', 'chicken', 'mix', 'italian', 'turkish']

print(f"The first three items of the list are: {pizzas[0:3]}")

print(f"The middle three items of the list are: {pizzas[2:5]}")

print(f"The last three items of the list are: {pizzas[3:]}")

print("---------TRY IT YOURSELF 4.11------------")

my_pizzas = ['meet', 'chicken', 'mix']

your_pizzas = my_pizzas[:]

my_pizzas.append('turkish')
for pizza in my_pizzas:
    print(pizza)
print(my_pizzas)

your_pizzas.append('italian')
for pizza in your_pizzas:
    print(pizza)
print(your_pizzas)

print("---------TRY IT YOURSELF 4.11------------")
menu = ('hilibgeel', 'suqaar', 'bariis', 'cambuulo', 'canjeero')
for cunto in menu:
    print(cunto)

menu = ('hilibari', 'suqaar', 'bariis', 'beer', 'canjeero')
print(menu)


print("---------TRY IT YOURSELF 5.1------------")
menu = ['hilibari', 'suqaar', 'bariis', 'beer', 'canjeero']
# casho = 'canbuulo'
if 'canjeero' and 'beer' in menu:
    print("waxay haysaa quraac fiican maqaayadani")


print("---------TRY IT YOURSELF 5.3------------")

alien_color1 = 'green'

if alien_color1 == 'red':
    print("the player has no points")

if alien_color1 == 'green':
    print("the player earned 5 points")
print("Game over")

print("---------TRY IT YOURSELF 5.4------------")

alien_color2 = 'yellow'

if alien_color2 == 'yellow':
    print("the player earned 5 points for shooting the alien")
else:
    print("the player just earned 10 points")

print("---------TRY IT YOURSELF 5.4------------")

if alien_color2 == 'yellow':
    print("the player earned 5 points for shooting the alien")
else:
    print("the player just earned 10 points")

print("---------TRY IT YOURSELF 5.5------------")

alien_colors = ['yellow', 'red5', 'greenn']
if 'red' in alien_colors :
    print("the player earned 5 points")
elif 'green' in alien_colors:
    print("the player earned 10 points")
elif 'yellow' in alien_colors:
    print("the player earned 15 points")
print("Game Over")
print()

print("---------TRY IT YOURSELF 5.6------------")
age = 15
if age < 2:
    print("You're a baby")
elif age < 4:
    print("You're a toddler")
elif age < 13:
    print("You're a kid")
elif age < 20:
    print("You're a teenager")
elif age < 65:
    print("You're a adult")
else:
    print("You're an elder")

print("---------TRY IT YOURSELF 5.7------------")

favorite_fruits = ['bananas', 'babaya', 'mango']
if 'bananas' in favorite_fruits:
    print(f"you like bananas")

if 'babaya' in favorite_fruits:
    print(f"you like babaya")

if 'mango' in favorite_fruits:
    print(f"you like mango")
print()


print("---------TRY IT YOURSELF 5.8------------")
usernames = ['jaden', 'bashir', 'sindra', 'kristian', 'marwan']
for user in usernames:
    if user == 'marwan':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"hello {user.title()}, thank you for logging in again!")
print()

print("---------TRY IT YOURSELF 5.9------------")
usernames = []
if usernames:
    for user in usernames:
        if user == 'marwan':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"hello {user.title()}, thank you for logging in again!")
else:
    print("We need to find some users!")
print()

print("---------TRY IT YOURSELF 5.10------------")

current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

current_users_lower = [usere.lower() for usere in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}, this user is not available")
    else:
        print(f"{new_user}, this user is available")



print("---------TRY IT YOURSELF 5.11------------")
ordinal_numbers = list(range(1,10))

for number in ordinal_numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")




