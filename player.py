# player class which inherits from pygame sprites
from Entity import Entity
#import health

class Player(Entity):
	
	def __init__(self, image_paths,fps=10):
		Entity.__init__(self,image_paths,(200,230),fps,1)
		#health = health.Health("Images//bone.png")	
		self.jumping = False # jumping flag
		self.can_jump = True
		self.y_vel = 0 # amount of jump movement per update
		self.health = 3

	def update(self,t=0):
		Entity.update(self,t)	
		if self.jumping:
			# if the jumping flag is true,
			# call the jump function
			self.jumping = False
			self.accel_delay = 0
			if self.rect.top < 2:
				self.rect.top = 0
				self.y_vel = 0
			else:
				self.rect.top -= 3
				self.y_vel = -5
		
		if self.rect.top < 230:
			if self.rect.top < 0:
				self.y_vel = 0
				self.rect.top = 0
				self.can_jump = False

			self.accel_delay -= 1
			if self.accel_delay <= 0:
				self.y_vel += 1
				self.accel_delay = 6
			
			self.rect = self.rect.move(0, self.y_vel) # move upwards by self.jump amount

		else:
			self.rect.top = 230
			self.can_jump = True

	def jump(self):
		"""function which makes the player 'jump'"""
		self.jumping = self.can_jump

	def decrementHealth(self):
		"""decrement the player's health"""
		self.health -= 1

	def getHealth(self):
		"""return the player's health"""
		return self.health
