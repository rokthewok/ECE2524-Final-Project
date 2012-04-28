#! /usr/bin/env python

# player class which inherits from pygame sprites
import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
	
	def __init__(self, filename):
		pygame.sprite.Sprite.__init__(self) # initialize the base class
		self.image = pygame.image.load(filename) # load an image for the character
		self.rect = self.image.get_rect() # get the enclosing rectangle for the image
		self.jumping = False # jumping flag
		self.jump = -4 # amount of jump movement per update
		self.jump_height = 0 # to keep track of the height jumped 
		
		self.rect = self.rect.move( 200, 200 ) # set start location

	def update(self):
		# self.rect = self.rect.move(self.move, 0)
		if self.jumping:
			# if the jumping flag is true,
			# call the jump function
			self._jump()

	def _jump(self):
		"""function which makes the player 'jump'"""
		self.rect = self.rect.move(0, self.jump) # move upwards by self.jump amount
		self.jump_height = self.jump_height + self.jump # change the total amount jumped thus far
		if self.jump_height < -40: # jump limit
			self.jump_height = -40
			self.jump = -self.jump
		
		if self.jump_height > 0: # stop jumping
			self.jump_height = 0
			self.jump = -self.jump
			self.jumping = False
