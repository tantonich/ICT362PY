class Restaurant():
	"""A simple attempt to model a restaurant."""

	def __init__(self, name, type):
		"""initialize name and type attributes."""
		self.name = name
		self.type = type

	def describe_restaurant(self):
		"""Print the restaurant name and type"""
		print(self.name.title() + " is a " + self.type.title() + "!")

	def open_restaurant(self):
		"""Print the restaurant is open"""
		print(self.name.title() + " is open!")