import pygame
from pygame.locals import *

# a class to handle drawing stats to the screen; namely, health and score
class StatCounter(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.font = pygame.font.Font( None, 18 )
		self.score = 0
		self.string = "Health: %d Score: %d" % (0,self.score)
		self.image = self.font.render( self.string, 1, (0,0,0), (255,255,255) ) # will make background semi transparent later
		self.rect = self.image.get_rect()
		self.rect.topleft = (850,20)

	def update(self, health, elapsed_time):
		self.score += elapsed_time / 10
		self.string = "Health: %d Score: %d" % (health, self.score)

		self.image = self.font.render( self.string, 1, (0,0,0), (255,255,255) )
		
