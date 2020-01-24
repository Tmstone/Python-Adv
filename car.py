# creating a car class and its instances

class Car():
    ''' A simple attempt to represent a car. '''
    def __init__(self, make, model, year):
        ''' Initialize attributes to describe a car. '''
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
        self.gas_tank = 20

    def get_descriptive_name(self):
        ''' Return a neatly formatted descriptive name. '''
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        ''' Print a statement showing the cars milage '''
        print(f'This car has {self.odometer}  miles on it.')

# Modify an attribute's value through a method 
    def update_odometer(self, mileage):
        ''' Set the odometer reading to a given value.
        Reject the change if it attampts to roll the odometer back.
        '''
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print('You can\'t roll back an odometer' )

# Incrementing an attribute's value through a method
    def increment_odometer(self, miles):
        ''' Add the given amount to the odometer reading '''
        self.odometer += miles
    
    def fill_gas_tank(self):
        print('This car has a ' + str(self.gas_tank) + ' tank.')

class Battery():
    def __init__(self, battery_size = 70):
        ''' initialize batteries attributes '''
        self.battery_size = battery_size

    def describe_battery(self):
        ''' Print a statement describing the batery size '''
        print('This car has a ' + str(self.battery_size) + '-KWh battery.')
    
    def get_range(self):
        ''' Print a statement about the range the battery provides. '''
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        
        message = "This car can go approximatley " + str(range)
        message += ' miles on a full charge.'
        print(message)

class ElectricCar(Car):
    ''' Represents objects of a car, specific to electric vehicles '''
    def __init__(self, make, model, year):
        ''' initialize attributes of the parent class. '''
        super().__init__(make, model, year)
        self.battery = Battery()
    
    def fill_gas_tank(self):
        ''' Electric cars don't have gas tanks.'''
        print('This car doesn\'t have a gas tank.')

class HybridCar(Car):
    ''' Represents objects of a car, specific to electric vehicles '''
    def __init__(self, make, model, year):
        ''' initialize attributes of the parent class. '''
        super().__init__(make, model, year)
        self.battery = Battery()

my_new_car = Car('Audi', 'A4', '2019')
print(my_new_car.get_descriptive_name())
#my_new_car.read_odometer()

#modify an attribute's value directly
my_new_car.odometer = 23
#my_new_car.read_odometer()
print()
my_used_car = Car('Subaru', 'outback', 2017)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23000)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
print()
#printing attributes of an electric car
my_tesla = ElectricCar('Tesla', 'Model S', 2019)
my_tesla.update_odometer(100)
print(my_tesla.get_descriptive_name())
my_tesla.read_odometer()
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
print()
my_hybrid = HybridCar('BMW', 'i7', 2020)
print(my_hybrid.get_descriptive_name())
my_hybrid.fill_gas_tank()
#my_hybrid.battery(battery_size = 50)
my_hybrid.battery.describe_battery()

