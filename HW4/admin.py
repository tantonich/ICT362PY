from user import User

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