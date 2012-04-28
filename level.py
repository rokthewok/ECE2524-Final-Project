#! /usr/bin/env python

# player class which inherits from pygame sprites
import pygame
from pygame.locals import *

class Level(pygame.sprite.Sprite):
	
	def __init__(self, filename):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(filename)
		self.rect = self.image.get_rect()
		self.move = -2 # amount of movement per update
		
		self.rect = self.rect.move( 0, 0 ) # set start location

	def update(self):
		self.rect = self.rect.move(self.move, 0)
