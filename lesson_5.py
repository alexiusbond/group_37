from random import randint as generate_number, choice
import calculator

from person import Person
from termcolor import cprint
import emoji
from decouple import config

print(generate_number(2, 10))
print(calculator.multiplication(4, 2))

friend = Person("Mark", 43)
print(friend)

cprint("Hello, World!", "green", "on_red")

print(emoji.emojize('Python is :thumbs_up:'))
# Hi sensei

print(config('DATABASE_URL'))
commented = config('COMMENTED', default=0, cast=int)
print(commented * 2)
