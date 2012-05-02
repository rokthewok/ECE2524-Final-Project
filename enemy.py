from Entity import Entity

class Enemy(Entity):

	def __init__(self, image_paths, fps=10):
		Entity.__init__(self,image_paths,(500,300),fps,1)
		self.moving = False
		self.moveSpeed = 0
		self.x_vel = 0

	def update(self,t=0):
		Entity.update(self,t)
		if self.moving:
			self.x_vel = self.moveSpeed
		else:
			self.x_vel = 0
		if self.rect.right < 0:
			self.moving = False

	def setEnemy(self, top, left, speed):
		self.moving = True
		self.rect.top = top
		self.rect.left = left
		self.moveSpeed = speed
