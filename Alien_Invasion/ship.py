import pygame
from pygame.sprite import Sprite

# Reference 4.3.k
class Ship(Sprite):
	"""A class to manage the ship."""
	# Reference 1.1.a

	def __init__(self, ai_game):
		"""Initialize the ship and set its starting position."""
		# Reference 4.3.k
		super().__init__()
		self.screen = ai_game.screen		
		# Reference 1.3.d
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		# Load the ship image and get its rect.
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		# Start each new ship at the bottom of the screen.
		self.rect.midbottom = self.screen_rect.midbottom

		# Reference 1.3.d
		# Store a decimal value for the ship's horizontal position.
		self.x = float(self.rect.x)

		# Movement flags
		# Reference 1.3.b		
		self.moving_right = False
		# Reference 1.3.c
		self.moving_left = False

	def update(self):
		"""Update the ship's position based on the movement flags."""
		# Reference 1.3.b, 1.3.e
		if self.moving_right and self.rect.right < self.screen_rect.right:
		# Reference 1.3.d
			self.x += self.settings.ship_speed
		# Reference 1.3.c, 1.3.e
		if self.moving_left and self.rect.left > 0:
		# Reference 1.3.d
			self.x -= self.settings.ship_speed
		
		# Update rect object from self.x.
		# Reference 1.3.d
		self.rect.x = self.x

	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

	# Reference 3.b
	def center_ship(self):
		"""Center the ship on the screen."""
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)