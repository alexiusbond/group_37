class Transport:
    def __init__(self, theModel, theYear, theColor):
        self.model = theModel
        self.year = theYear
        self.color = theColor

    # method
    def change_color(self, new_color):
        self.color = new_color


class Plane(Transport):
    def __init__(self, theModel, theYear, theColor):
        super().__init__(theModel, theYear, theColor)


class Car(Transport):
    counter = 0
    standart_number_of_wheel = 4

    # constructor
    def __init__(self, theModel, theYear, theColor, penalties=0):
        # attributes / fields
        super().__init__(theModel, theYear, theColor)
        self.penalties = penalties
        Car.counter += 1

    # method
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')


class Truck(Car):
    standart_number_of_wheel = 10
    def __init__(self, theModel, theYear, theColor,
                 penalties=0, load_capacity=0):
        super().__init__(theModel, theYear, theColor, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, weight, type):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity} kg')
        else:
            print(f'You successfully loaded cargo of {type} ({weight} kg.)')


price_of_lastic = 5000
print(f'Fabric CAR produced: {Car.counter} cars.')
print(f'We need '
      f'{price_of_lastic * Car.counter * Car.standart_number_of_wheel}'
      f' soms.')

bmw_car = Car('BMW X7', 2020, 'Black')
print(bmw_car)
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} COLOR: {bmw_car.color} '
      f'PENALTIES: {bmw_car.penalties}')
# bmw_car.color = 'Red'
bmw_car.change_color('Red')
print(f'MODEL: {bmw_car.model} YEAR: {bmw_car.year} '
      f'NEW COLOR: {bmw_car.color} PENALTIES: {bmw_car.penalties}')

honda_car = Car(theColor='Green', penalties=1200,
                theModel='Honda Civic', theYear=2000)
print(f'MODEL: {honda_car.model} YEAR: {honda_car.year} COLOR: {honda_car.color} '
      f'PENALTIES: {honda_car.penalties}')

honda_car.drive('Osh')
bmw_car.drive('Kant')
bmw_car.drive('Tokmok')

print(f'Fabric CAR produced: {Car.counter} cars.')
print(f'We need '
      f'{price_of_lastic * Car.counter * Car.standart_number_of_wheel}'
      f' soms.')

su_125_plane = Plane('SU 125', 2022, 'White')
print(f'MODEL: {su_125_plane.model} YEAR: {su_125_plane.year} '
      f'COLOR: {su_125_plane.color}')

kamaz_truck = Truck('Kamaz 100', 1990, 'Orange',
                    900, 30000)
print(f'MODEL: {kamaz_truck.model} YEAR: {kamaz_truck.year} '
      f'COLOR: {kamaz_truck.color} PENALTIES: {kamaz_truck.penalties} '
      f'LOAD CAPACITY: {kamaz_truck.load_capacity} kg')
kamaz_truck.load_cargo(35000, 'apples')
kamaz_truck.load_cargo(25000, 'tomatoes')
kamaz_truck.drive('Batken')

print(f'Truck has {Truck.standart_number_of_wheel} wheels.')