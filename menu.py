import pygame,sys
from pygame.locals import *

class Menu(pygame.sprite.Sprite):

	def __init__(self,filename):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(filename)
		self.rect = self.image.get_rect()
		self.running = True

	def menu(self, screen):
		"""function to show the menu"""
		screen.blit(self.image, (0,0))
		pygame.display.flip()
		while self.running:
			event = pygame.event.poll()
			if event.type == MOUSEBUTTONDOWN:
				location = pygame.mouse.get_pos()
				# print location
				if location[0] > 350 and location[0] < 625  and \
				location[1] > 265 and location[1] < 300:
					self.running = False

			if event.type == QUIT:
				sys.exit(0)

class PauseMenu(pygame.sprite.Sprite):

	def __init__(self,filename):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(filename)
		self.rect = self.image.get_rect()
		self.running = True

	def menu(self,screen):
		"""shows the pause menu"""
		self.running = True
		screen.blit(self.image, (0,0))
		pygame.display.flip()
		while self.running:
			event = pygame.event.poll()
			if event.type == MOUSEBUTTONDOWN:
				location = pygame.mouse.get_pos()
				
				# resume
				if location[0] > 381 and location[0] < 610:
					# resume
					if location[1] > 243 and location[1] < 286:
						self.running = False
				
					# exit
					if location[1] > 302 and location[1] < 342:
						sys.exit(0)

			if event.type == QUIT:
				sys.exit(0)

			if event.type == KEYDOWN and event.key == K_ESCAPE:
				self.running = False
