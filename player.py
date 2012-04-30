# player class which inherits from pygame sprites
from Entity import Entity

class Player(Entity):
	
	def __init__(self, image_paths,fps=10):
		Entity.__init__(self,image_paths,[200,200],fps)	
		self.jumping = False # jumping flag
		self.can_jump = True
		self.y_vel = 0 # amount of jump movement per update

	def update(self,t=0):
		Entity.update(self,t)	
		if self.jumping:
			# if the jumping flag is true,
			# call the jump function
			self.y_vel = -5
			self.jumping = False
			self.accel_delay = 0
			self.rect.top -= 3
		
		if self.rect.top < 200:
			if self.rect.top < 0:
				self.y_vel = 0
				self.can_jump = False

			self.accel_delay -= 1
			if self.accel_delay <= 0:
				self.y_vel += 1
				self.accel_delay = 6
			
			self.rect = self.rect.move(0, self.y_vel) # move upwards by self.jump amount
		else:
			self.rect.top = 200
			self.can_jump = True

	def jump(self):
		"""function which makes the player 'jump'"""
		self.jumping = self.can_jump
