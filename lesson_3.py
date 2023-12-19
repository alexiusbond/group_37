from enum import Enum


class Color(Enum):
    RED = '\33[31m'
    GREEN = '\33[32m'
    BLUE = '\33[34m'
    YELLOW = '\33[33m'
    VIOLET = '\33[35m'


# Mixin
class MusicPlayable:
    # def __init__(self):
    #     pass

    def play_music(self, song):
        print(f'Now is playing {song}')

    def stop_music(self):
        print('Music stopped')


class Drawable:
    def draw(self, emoji):
        print(f'{emoji}')


class SmartPhone(MusicPlayable, Drawable):
    pass


class Car(MusicPlayable, Drawable):
    def __init__(self, model, year, color):
        self.__model = model
        self.__year = year
        if type(color) == Color:
            self.__color = color
        else:
            raise ValueError('Wrong color type')

    @property
    def model(self):
        return self.__model

    @property
    def year(self):
        return self.__year

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def drive(self):
        print(f'Car {self.__model} is driving')

    def __str__(self):
        return (f'Model: {self.__model}, Year: {self.__year} '
                f'Color: {self.__color.value}{self.__color.name} '
                f'\33[0m')

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year

    def __lt__(self, other):
        return self.year < other.year

    def __le__(self, other):
        return self.year <= other.year

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year


class FuelCar(Car):
    __total_fuel_amount = 1000

    @classmethod
    def get_total_fuel_amount(cls):
        return cls.__total_fuel_amount

    @classmethod
    def fill_fuel_amount(cls, amount):
        cls.__total_fuel_amount += amount

    @staticmethod
    def get_fuel_type():
        return 'AI 98'

    def __init__(self, model, year, color, fuel_bank):
        Car.__init__(self, model, year, color)
        self.__fuel_bank = fuel_bank
        FuelCar.__total_fuel_amount -= self.__fuel_bank

    @property
    def fuel_bank(self):
        return self.__fuel_bank

    def drive(self):
        print(f'Car {self.model} is driving by using fuel')

    def __str__(self):
        return super().__str__() + f' Fuel Bank: {self.__fuel_bank}'

    def __add__(self, other):
        return str(self.__fuel_bank + other.__fuel_bank) + f' liters.'


class ElectricCar(Car):
    def __init__(self, model, year, color, battery):
        Car.__init__(self, model, year, color)
        self.__battery = battery

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def drive(self):
        print(f'Car {self.model} is driving by using electricity')

    def __str__(self):
        return super().__str__() + f' Battery: {self.__battery}'


class HybridCar(FuelCar, ElectricCar):
    def __init__(self, model, year, color, fuel_bank, battery):
        FuelCar.__init__(self, model, year, color, fuel_bank)
        ElectricCar.__init__(self, model, year, color, battery)


print(f'Fabric FUEL_CAR has: {FuelCar.get_total_fuel_amount()} liters.')

car = Car('Audi A6', 2009, Color.GREEN)
print(car)

fuel_car = FuelCar('BMW X7', 2023, Color.BLUE, 80)
print(fuel_car)

electric_car = ElectricCar('Tesla Model X', 2022,
                           Color.RED, 25000)
print(electric_car)

hybrid_car = HybridCar('Toyota Camry 70', 2020, Color.YELLOW,
                       70, 15000)

hybrid_car_2 = HybridCar('Toyota Corolla', 2021, Color.VIOLET,
                         60, 13000)
print(hybrid_car)
hybrid_car.drive()

print(HybridCar.mro())
number_1 = 6
number_2 = 1
print(f'Number 1 is greater than Number 2: {number_1 > number_2}')
print(f'Number 1 is less than Number 2: {number_1 < number_2}')
print(f'Hybrid car is better than Fuel car: {hybrid_car > fuel_car}')
print(f'Hybrid car is not the same with Fuel car: {hybrid_car != fuel_car}')

print(f'Sum of all numbers: {number_1 + number_2}')
print(f'{fuel_car + hybrid_car}')

# FuelCar.total_fuel_amount -= 100
FuelCar.fill_fuel_amount(500)
print(f'Fabric FUEL_CAR has: {FuelCar.get_total_fuel_amount()} '
      f'({FuelCar.get_fuel_type()}) liters.')

hybrid_car_2.play_music('Best song')
samsung_phone = SmartPhone()
samsung_phone.play_music('Song 1')
samsung_phone.stop_music()

hybrid_car_2.draw('🚗')
samsung_phone.draw('📱')

if electric_car.model == 'Tesla Model X':
    print('This car is cool')

if electric_car.color == Color.RED:
    print('This car is beautiful')
