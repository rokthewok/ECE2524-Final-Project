import pygame

class Entity(pygame.sprite.Sprite):
	def __init__(self,image_paths,initial_pos,fps = 10, animEnd = 0):
		#Call Sprite Constructor
		pygame.sprite.Sprite.__init__(self)
		self._delay = 1000/fps
		self._last_update = 0
		self._frame = 0
		self._startFrame = 0 #The start image of anim loop (zero-indexed)
		self._endFrame = animEnd #The end image of anim loop (zero-indexed)
		self._images = []
		
		#Set up the speed and decay speed defaults (set to a number over 1 to
		#			cause a speed up)
		self._speed = [0.0,0.0]
		self._speedDecay = [1.0, 1.0]

		#Load images and store in _images
		for image in image_paths:
			self._images.append( pygame.image.load(image) )
		#Set Image to first image
		self.image = self._images[0]
		#Set Position		
		self.rect = self.image.get_rect()
		self.rect.inflate_ip( -self.rect.width / 2, -self.rect.height / 2 ) # shrink the hit box
		self.rect.topleft = initial_pos		

	def update(self,t):
		#print self._last_update
		self._last_update += t
		if self._last_update > self._delay:
			self._frame += 1
			if self._frame > self._endFrame:
				self._frame = self._startFrame
			
			self.image = self._images[self._frame]
			self._last_update = 0
		
		#Cause decay of speed (if it is set to decay)
		# Note: Can cause things to speed up too
		self._speed[0] *= self._speedDecay[0]
		self._speed[1] *= self._speedDecay[1]
		#move the entity
		dx = float((t/100.0)*self._speed[0])
		dy = float((t/100.0)*self._speed[1])
		self.rect.move_ip(dx,dy)
		#check y bounds
		if self.rect.top < 0:
			self.rect.top = 0
		if self.rect.top > 230:
			self.rect.top = 230
	
	def moveHoriz(self, dx):
		"""Adds the provided value to the entity's x velocity"""
		self._speed[0] += dx
	
	def setSpeed(self,x,y):
		"""Sets the provided speed to the provided value. If you don't want to
		change the value, pass in 'x' for the parameter"""
		if not x=='x':
			self._speed[0] = float(x)	
		if not y=='x':
			self._speed[1] = float(y)	

	def setAnim(self,start,end):
		self._startFrame = 0
		self._endFrame = 0
		length=len(self._images)-1
		if (length >= end)and(length >= start)and(end-start >= 0):
			self._startFrame = start
			self._endFrame = end

	def action(self,thing=None):
		"Generic Action Stuff Here"
