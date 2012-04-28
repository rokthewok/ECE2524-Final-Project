# player class which inherits from pygame sprites
import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
	
	def __init__(self, filename):
		pygame.sprite.Sprite.__init__(self) # initialize the base class
		self.image = pygame.image.load(filename) # load an image for the character
		self.rect = self.image.get_rect() # get the enclosing rectangle for the image
		self.jumping = False # jumping flag
		self.can_jump = True
		self.y_vel = 0 # amount of jump movement per update
		
		self.rect = self.rect.move( 200, 200 ) # set start location

	def update(self):
		if self.jumping:
			# if the jumping flag is true,
			# call the jump function
			self.y_vel = -5
			self.jumping = False
			self.accel_delay = 0
			self.rect.top -= 3
		
		if self.rect.top < 200:
			if self.rect.top < 0:
				self.y_vel = 0
				self.can_jump = False

			self.accel_delay -= 1
			if self.accel_delay <= 0:
				self.y_vel += 1
				self.accel_delay = 6
			
			self.rect = self.rect.move(0, self.y_vel) # move upwards by self.jump amount
		else:
			self.rect.top = 200
			self.can_jump = True

	def jump(self):
		"""function which makes the player 'jump'"""
		self.jumping = self.can_jump
