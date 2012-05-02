# player class which inherits from pygame sprites
from Entity import Entity
#import health

class Player(Entity):
	
	def __init__(self, image_paths,fps=10):
		Entity.__init__(self,image_paths,(200,230),fps,1)
		#health = health.Health("Images//bone.png")	
		self.jumping = False # jumping flag
		self.can_jump = True
		self.health = 3

	def update(self,t=0):
		Entity.update(self,t)
		print t, self.rect.topleft, self._speed 
		if self.jumping:
			# if the jumping flag is true,
			# call the jump function
			self._speed[1] = -15.0
			self.jumping = False
		else:
			self.can_jump = True
			self._speed[1] += t/50.0	
			if self.rect.top >= 230:
				self._speed[1] = 0.0

	def jump(self):
		"""function which makes the player 'jump'"""	
		if self.rect.top < 2:
			self.can_jump = False
		self.jumping = self.can_jump

	def decrementHealth(self):
		"""decrement the player's health"""
		self.health -= 1

	def getHealth(self):
		"""return the player's health"""
		return self.health
