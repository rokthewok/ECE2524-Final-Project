#! /usr/bin/env python

# player class which inherits from pygame sprites
import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
	
	def __init__(self, filename):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(filename)
		self.rect = self.image.get_rect()
		self.jumping = False
		self.jump = -4 # amount of jump movement per update
		self.jump_height = 0 # to keep track of the height jumped 
		self.move = 5 # amount of movement per update
		
		self.rect = self.rect.move( 200, 200 ) # set start location

	def update(self):
		self.rect = self.rect.move(self.move, 0)
		if self.jumping:
			# if the jumping flag is true,
			# call the jump function
			self._jump()

	def _jump(self):
		self.rect = self.rect.move(0, self.jump)
		self.jump_height = self.jump_height + self.jump
		if self.jump_height < -40:
			self.jump_height = -40
			self.jump = -self.jump
		
		if self.jump_height > 0:
			self.jump_height = 0
			self.jump = -self.jump
			self.jumping = False
