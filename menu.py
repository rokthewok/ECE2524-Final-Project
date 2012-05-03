import pygame,sys
from pygame.locals import *

class Menu(pygame.sprite.Sprite):

	def __init__(self,filename,audio_file):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(filename)
		self.rect = self.image.get_rect()
		self.running = True
		self.music_file = audio_file

	def menu(self, screen):
		"""function to show the menu"""
		screen.blit(self.image, (0,0))
		pygame.display.flip()
		pygame.mixer.music.load( self.music_file )
		pygame.mixer.music.set_volume(0.7)
		pygame.mixer.music.play(-1)
		self.running = True

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
		pygame.mixer.music.stop()

class PauseMenu(pygame.sprite.Sprite):

	def __init__(self,filename):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(filename)
		self.rect = self.image.get_rect()
		self.running = True

	def menu(self,screen,clock):
		"""shows the pause menu"""
		pygame.mixer.music.set_volume(0.2)
		self.running = True
		screen.blit(self.image, (0,0))
		pygame.display.flip()

		while self.running:
			clock.tick(60) # keep the clock ticking
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

		pygame.mixer.music.set_volume(1)

class GameOverMenu(pygame.sprite.Sprite):

	def __init__(self, filename):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(filename)
		self.rect = self.image.get_rect()
		self.running = True

	def menu(self, screen):
		screen.blit(self.image, (0,0))
		self.running = True
		pygame.mixer.music.stop()
		pygame.display.flip()

		while self.running:
			event = pygame.event.poll()
			if event.type == MOUSEBUTTONDOWN:
				location = pygame.mouse.get_pos()

				if location[0] > 160 and location[0] < 417:
					# main menu
					if location[1] > 200 and location[1] < 260:
						return True
					# exit
					if location[1] > 285 and location[1] < 340:
						return False
				
			if event.type == QUIT:
				sys.exit(0)
