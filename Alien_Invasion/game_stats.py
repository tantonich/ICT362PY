# Reference 3.c
class GameStats:
	"""Track statistics for Alien Invasion."""

	def __init__(self, ai_game):
		"""Initialize statistics."""
		self.settings = ai_game.settings
		self.reset_stats()

		# Reference 3.e, 4.1
		# Start Alien Invasion in an inactive state.
		self.game_active = False

		# Reference 4.3.i
		# High score should never be reset.
		self.high_score = 0	

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.settings.ship_limit
		# Reference 4.3.a
		self.score = 0
		# Reference 4.3.j
		self.level = 1