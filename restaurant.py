class Restaurant():
    ##restaurant class ##
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(self.name.title() + " produces " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The " + self.name.title() + " is open.")

    def service(self):
        ''' Print a statement showing the number of customers served '''
        print(f'{self.name} has served {self.number_served} customers.\n')

# adding method set_nummber_served
    def set_number_served(self, number):
        number = self.number_served

# adding a method to increment_number_served
    def increment_number_served(self, customers):
        self.number_served += customers

class IceCreamStand(Restaurant):
    ''' Represents objects of the restaurant specific to an ice cream stand '''
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = ""

new_restaurant = Restaurant('Dat Jerk', 'Caribbean Food')
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()
new_restaurant.increment_number_served(30)
new_restaurant.service()

my_restaurant = Restaurant('Noodles & Co', 'Fusion Pasta Meals')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.increment_number_served(100)
my_restaurant.service()

her_restaurant = Restaurant('Panda Express', 'Asian Food')
her_restaurant.describe_restaurant()
her_restaurant.open_restaurant()
her_restaurant.increment_number_served(300)
her_restaurant.service()

my_iceCream = IceCreamStand('Dipping Dots', 'Ice Cream Pellets')
my_iceCream.describe_restaurant()
my_iceCream.open_restaurant()
