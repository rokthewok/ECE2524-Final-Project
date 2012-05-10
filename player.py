# player class which inherits from pygame sprites
import pygame
from Entity import Entity
#import health

class Player(Entity):
	
	def __init__(self, image_paths,fps=10):
		Entity.__init__(self,image_paths,(200,230),fps,1)	
		self.jumping = False # jumping flag
		self.health = 10
		self._invincible = False # for when player collides with an enemy
		self._invincible_time = 0 # timer for invincibility
		
		# Set up the decay for left and right movement
		self._speedDecay = [0.9, 1.0]
		
		# Precalculate the invisible image for when the dog is invincible
		self._invisible_pic = self.image.copy()
		self._invisible_pic.fill([0,0,0,0])

		# scale images for player
		image_set = []
		for image in self._images:
			image_set.append( ( pygame.transform.scale( image, (130,67) ) ) )
		self._images = image_set
		self._rect = self._images[0].get_rect()
		self._rect.inflate_ip( -self._rect.width / 2, -self._rect.height / 2 )
	
	def update(self,t=0):
		Entity.update(self,t)
		#print t, self.rect.topleft, self._speed 
		if self.jumping:
			# if the jumping flag is true,
			# call the jump function
			self.setSpeed('x',-14.0)
			self.jumping = False
		else:
			self.setSpeed('x',self._speed[1]+t/50.0)	
			if self.rect.top >= 230: # if you hit the top, reset the vel so it
				self.setSpeed('x',0.0) # doesn't get stuck up at the top

		# limit duration of post damage invincibility (2500 ms)
		if self._invincible_time > 0:
			self._invincible_time -= t
			
			# On average, turn invisible for every other frame
			if ((self._invincible_time /100)%2) == 0:
				self.image = self._invisible_pic
			else:
				self.image = self._images[0]
		
		if self.rect.left < 0:
			self.rect.left = 0
		elif self.rect.right > 930:
			self.rect.right = 930
	
	def jump(self):
		"""function which makes the player 'jump'"""
		if self.rect.top >= 2: #Only jump if you're not hitting the ceiling
			self.jumping = True

	def takeDamage(self):
		"""Causes player to take damage"""
		if self._invincible_time <= 0:
			self.health -= 1
			# make player invincible
			self._invincible_time = 2500 # invincible for 2.5s

	def healHealth(self):
		"""Player gains health by touching a bone"""
		self.health += 1

	def getHealth(self):
		"""return the player's health"""
		return self.health

	def resetHealth(self):
		"""reset the player's health to full value"""
		self.health = 10
