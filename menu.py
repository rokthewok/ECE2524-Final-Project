import pygame
from pygame.locals import *

class Menu(pygame.sprite.Sprite):

	def __init__(self,filename):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(filename)
		self.rect = self.image.get_rect()
		self.running = True

	def menu(self, screen):
		"""function to show the menu"""
		while self.running:
			screen.blit(self.image, (0,0))
			pygame.display.flip()
			event = pygame.event.poll()
			if event.type == MOUSEBUTTONDOWN:
				location = pygame.mouse.get_pos()
				# print location
				if location[0] > 350 and location[0] < 625  and \
				location[1] > 265 and location[1] < 300:
					self.running = False

