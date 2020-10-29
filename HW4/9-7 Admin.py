# 9-5 login attempts
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

class Privileges():
	"""A class just for privileges"""
	def __init__(self):
		"""Initialize privileges"""
		self.privileges = ['can add post', 'can delete post', 'can ban user']

	def show_privileges(self):
		"""Print the privelages of Admin class"""
		admin_privileges = self.privileges
		print("The Admin can do the following actions:")
		for privilege in admin_privileges:
			print(privilege.title())

class Admin(User):
	"""includes admin privileges"""

	def __init__(self, first_name, last_name, screen_name, expiration):
		"""Inherits the User class attributes and gives admin attributes"""
		super().__init__(first_name, last_name, screen_name, expiration)
		self.privileges = Privileges()


user1 = User('taylor', 'antonich', 'tantonich', 'january 1, 2021')
admin1 = Admin('super', 'user', 'su', 'never')
admin1.privileges.show_privileges()
# admin1.describe_user()
# user1.describe_user()
# user2 = User('joe', 'shmo', 'jshmo', 'december 30, 2020')
# user2.describe_user()
# user2.increment_login_attempts()
# user2.increment_login_attempts()
# user2.increment_login_attempts()
# print(str(user2.login_attempts))
# user2.reset_login_attempts()
# print(str(user2.login_attempts))
