import pygame
from pygame.locals import *

class Level(object):

	def __init__(self, bkgd_filename, midgd_filename, music_file):
		self._image0 = pygame.image.load(bkgd_filename)
		self._image1 = pygame.image.load(bkgd_filename)
		self._mid_image0 = pygame.image.load(midgd_filename)
		self._mid_image1 = pygame.image.load(midgd_filename)
		
		self._rect0 = self._image0.get_rect(topleft=(0,0))
		self._rect1 = self._image1.get_rect(topleft=(2048,0))
		self._mid_rect0 = self._mid_image0.get_rect(topleft=(0,0))
		self._mid_rect1 = self._mid_image1.get_rect(topleft=(2048,0))

		self.move = -1
		self.mid_move = -2
		
		# once we have music, this will play it for the level
		#self.music = pygame.mixer.music.load(music_file)
		#self.music.pygame.mixer.music.play(-1) # loop infinitely

	def update(self):
		# checks to see if the background has scrolled off the screen; if it has, move it back to the start
		if self._rect0.right == 0:
			self._rect0.left = 2048
		if self._rect1.right == 0:
			self._rect1.left = 2048
		
		if self._mid_rect0.right == 0:
			self._mid_rect0.left = 2048
		if self._mid_rect1.right == 0:
			self._mid_rect1.left = 2048

		self._rect0 = self._rect0.move( self.move, 0 )
		self._rect1 = self._rect1.move( self.move, 0 )
		
		self._mid_rect0 = self._mid_rect0.move( self.mid_move, 0 )
		self._mid_rect1 = self._mid_rect1.move( self.mid_move, 0 )
	
	def draw(self,screen):
		screen.blit( self._image0, self._rect0 )
		screen.blit( self._image1, self._rect1 )

		screen.blit( self._mid_image0, self._mid_rect0 )
		screen.blit( self._mid_image1, self._mid_rect1 )
