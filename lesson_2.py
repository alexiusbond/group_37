class Contact:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        self.__number = number

    @property
    def city(self):
        return self.__city

    @property
    def street(self):
        return self.__street

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value):
        self.__number = value


class Animal:
    def __init__(self, name, age, contact: Contact):
        self.__name = name
        if type(age) == int and age > 0:
            self.__age = age
        else:
            raise ValueError('Wrong value for attribute age. It must be positive number.')
        if type(contact) == Contact:
            self.__contact = contact
        else:
            raise ValueError('Wrong value for attribute contact. It must be of data type Contact.')
        self.__was_born()

    def __was_born(self):
        print(f'Animal {self.__name} was born.')

    def set_name(self, new_name):
        self.__name = new_name

    def set_age(self, new_age):
        if type(new_age) == int and new_age > 0:
            self.__age = new_age
        else:
            raise ValueError('Wrong value for attribute age. It must be positive number.')

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def info(self):
        return (f'NAME: {self.__name} AGE: {self.__age} '
                f'BIRTH YEAR: {2023 - self.__age} '
                f'\nCONTACT INFO: {self.__contact.city}, '
                f'{self.__contact.street} {self.__contact.number}')
    def speak(self):
        raise NotImplementedError('Method speak must be implement')

class Dog(Animal):
    def __init__(self, name, age, commands, contact):
        super(Dog, self).__init__(name, age, contact)
        self.__commands = commands

    def speak(self):
        print('Gav')

    @property
    def commands(self):
        return self.__commands

    @commands.setter
    def commands(self, value):
        self.__commands = value

    def info(self):
        return super().info() + f'\nCOMMANDS: {self.__commands}'


class FightingDog(Dog):
    def __init__(self, name, age, commands, wins, contact):
        super(FightingDog, self).__init__(name, age, commands, contact)
        self.__wins = wins

    def speak(self):
        print('Rrrrr gav')

    @property
    def wins(self):
        return self.__wins

    @wins.setter
    def wins(self, value):
        self.__wins = value

    def info(self):
        return super().info() + f'\nWINS: {self.__wins}'


class Cat(Animal):
    def __init__(self, name, age, contact):
        super(Cat, self).__init__(name, age, contact)

    def speak(self):
        print('Myau')


class Fish(Animal):
    def __init__(self, name, age, contact):
        super(Fish, self).__init__(name, age, contact)

    def speak(self):
        pass

# some_aminal = Animal('Anim', 2)
# some_aminal.set_age(3)
# print(some_aminal.info())
# print(some_aminal.get_name())

my_contact = Contact('Bishkek', 'Isanova', 1)

snooppy_dog = Dog('Snooppy', 4, 'Sit', my_contact)
# snooppy_dog.commands = 'Sit, run'
# print(snooppy_dog.commands)
# print(snooppy_dog.info())

taison_fdog = FightingDog('Taison', 1,
                          'Fight', 1, my_contact)
# taison_fdog.wins = 12
# print(taison_fdog.info())

# contact_2 = Contact('Osh', 'Manasa', 7)
#       a = b
cat = Cat('Tom', 2, Contact('Osh', 'Manasa', 7))
# print(cat.info())

# my_contact.number = 33
# print(taison_fdog.info())
# print(snooppy_dog.info())

fish = Fish('Sten', 15, my_contact)

animal_list = [snooppy_dog, fish, taison_fdog, cat]
for animal in animal_list:
    print(animal.info())
    animal.speak()
