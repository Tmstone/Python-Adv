class Restaurant():
    ##restaurant class ##
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        print(self.name.title() + " produces " + self.cuisine_type + ".")

    def open_restaurant(self):
        print("The " + self.name.title() + " is open.\n")


new_restaurant = Restaurant('Dat Jerk', 'Caribbean Food')
new_restaurant.describe_restaurant()
new_restaurant.open_restaurant()

my_restaurant = Restaurant('Noodles & Co', 'Fusion Pasta Meals')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

her_restaurant = Restaurant('Panda Express', 'Asian Food')
her_restaurant.describe_restaurant()
her_restaurant.open_restaurant()