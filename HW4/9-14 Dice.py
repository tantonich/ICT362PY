from random import randint
class Die():
	"""A class for random dice"""
	def __init__(self, sides=6):
		"""Initialize sides of dice"""
		self.sides = sides

	def roll_die(self):
		"""method to generate a dice roll"""
		x = randint(1,self.sides)
		print(str(x))
roll = Die()
roll.roll_die()

roll_10 = Die(10)
for value in range(1,11):
	roll_10.roll_die()

roll_20 = Die(20)
for value in range(1,11):
	roll_20.roll_die()