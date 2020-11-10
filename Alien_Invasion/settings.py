class Settings():
	"""A class to store all settings for Alien Invasion."""

	def __init__(self):
		"""Initialize the game's settings."""
		# Screen Settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Ship settings
		# Reference 1.3.d
		self.ship_speed = 1.5
		# Reference 3.b
		self.ship_limit = 3

		# Reference 1.4.a, 2.4.c
		# Bullet settings
		self.bullet_speed = 1.5
		self.bullet_width = 30
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		# Reference 1.4.f
		self.bullets_allowed = 3

		# Reference 2.3.a, 2.3.b
		# Alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 1
		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		# Reference 4.2.a
		# How quickly the game speeds up
		self.speedup_scale = 1.1

		# Reference 4.3.g
		# How quickly the alien point values increase
		self.score_scale = 1.5

		# Reference 4.2.a
		self.initialize_dynamic_settings()

	# Reference 4.2.a
	def initialize_dynamic_settings(self):
		"""Initialize settings that change throughout the game."""
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.0

		# fleet_direction of 1 represents right; -1 represents left.
		self.fleet_direction = 1

		# Reference 4.1.d
		# Scoring
		self.alien_points = 50

	# Reference 4.2.a, 4.3.g
	def increase_speed(self):
		"""Increase speed settings and alien point values."""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale

		# Reference 4.3.g
		self.alien_points = int(self.alien_points * self.score_scale)
