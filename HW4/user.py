class User():
	"""A simple attempt to model a user."""

	def __init__(self, first_name, last_name, screen_name, expiration):
		"""initialize first and last name attributes."""
		self.first_name = first_name
		self.last_name = last_name
		self.screen_name = screen_name
		self.expiration = expiration
		self.login_attempts = 0

	def describe_user(self):
		"""Print the restaurant name and type"""
		full_name = self.first_name.title() + " " + self.last_name.title()
		print(full_name)
		print(self.screen_name + " expires on " + self.expiration)

	def increment_login_attempts(self):
		"""Increment the value of login_attempts by 1"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""Reset the value of login_attempts to 0"""
		self.login_attempts = 0