# player class which inherits from pygame sprites
import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
	
	def __init__(self, filename1, filename2):
		pygame.sprite.Sprite.__init__(self) # initialize the base class
		self._image0 = pygame.image.load(filename1) # load an image for the character
		self._image1 = pygame.image.load(filename2) # load an image for the character
		self.image = self._image0
		
		self.rect = self.image.get_rect() # get the enclosing rectangle for the image
		self.jumping = False # jumping flag
		self.can_jump = True
		self.y_vel = 0 # amount of jump movement per update
		
		self.rect = self.rect.move( 200, 200 ) # set start location

		self.cur_image = 0
		self.animation_count = 0

	def update(self):
		self.animation_count -= 1
		if self.animation_count <= 0:
			self.animation_count = 20
			self.cur_image = (self.cur_image + 1) % 2

			if self.cur_image == 0:
				self.image = self._image0
			else:
				self.image = self._image1
		
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
