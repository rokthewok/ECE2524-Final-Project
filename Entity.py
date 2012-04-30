import pygame

class Entity(pygame.sprite.Sprite):
	def __init__(self,image_paths,initial_pos,fps = 10):
		#Call Sprite Constructor
		pygame.sprite.Sprite.__init__(self)
		self._delay = 1000/fps
		self._last_update = 0
		self._frame = 0
		self._images = []
		#Load images and store in _images
		for image in image_paths:
			self._images.append( pygame.image.load(image) )
		#Set Image to first image
		self.image = self._images[0]
		#Set Position		
		self.rect = self.image.get_rect()
		self.rect.topleft = initial_pos

	def update(self,t):
		#print self._last_update
		self._last_update += t
		if self._last_update > self._delay:
			self._frame += 1
			if self._frame >= len(self._images):
				self._frame = 0
			
			self.image = self._images[self._frame]
			self._last_update = 0