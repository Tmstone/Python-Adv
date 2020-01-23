# creating a car class and its instances

class Car():
    ''' A simple attempt to represent a car. '''
    def __init__(self, make, model, year):
        ''' Initialize attributes to describe a car. '''
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

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

my_new_car = Car('Audi', 'A4', '2019')
print(my_new_car.get_descriptive_name())
#my_new_car.read_odometer()

#modify an attribute's value directly
my_new_car.odometer = 23
#my_new_car.read_odometer()

my_used_car = Car('Subaru', 'outback', 2017)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23000)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()