# 9-4 Number Served
class Restaurant():
	"""A simple attempt to model a restaurant."""

	def __init__(self, name, type):
		"""initialize name and type attributes."""
		self.name = name
		self.type = type
		self.number_served = 0

	def describe_restaurant(self):
		"""Print the restaurant name and type"""
		print(self.name.title() + " is a " + self.type.title() + "!")

	def open_restaurant(self):
		"""Print the restaurant is open"""
		print(self.name.title() + " is open!")

	def number_customers(self):
		"""Print the number of customers served"""
		print("This restaurant has served " + str(self.number_served) + " customers.")

	def set_number_served(self, customers):
		"""Method that lets you set the number of customers that have been served"""
		self.number_served += customers

class IceCreamStand(Restaurant):
	"""A simple attempt to model an Ice Cream Stand."""

	def __init__(self, name, type):
		"""
		Initialize attributes of the parent class.
		Then initialize attributes specific to an electric car.
		"""
		super().__init__(name, type)
		self.flavors = ['strawberry', 'vanilla']

	def list_flavors(self):
		"""This method will list the flavor we have"""
		our_flavors = self.flavors
		print("Our flavors of ice cream are:")
		for flavor in our_flavors:
			print(flavor.title())

my_ice_cream_stand = IceCreamStand('frosty', 'ice cream stand')
my_ice_cream_stand.list_flavors()

# restaurant = Restaurant('dions', 'pizzaria')
# restaurant.describe_restaurant()
# restaurant.open_restaurant()
# restaurant.number_customers()
# restaurant.number_served = 3
# restaurant.number_customers()
# restaurant.set_number_served(6)
# restaurant.number_customers()
# restaurant1 = Restaurant('Sadies', 'new mexican food')
# restaurant1.describe_restaurant()
# restaurant2 = Restaurant('sonic', 'drive-thru')
# restaurant2.describe_restaurant()