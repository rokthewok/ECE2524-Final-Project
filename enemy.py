from Entity import Entity

class Enemy(Entity):

	def __init__(self, image_paths, fps=10):
		Entity.__init__(self,image_paths,(0,0),fps,1)
		self.moving = False
		self.moveSpeed = 0
		self.x_vel = 0

	def update(self,t=0):
		Entity.update(self,t)
		if self.moving:
			self.rect.left += self.moveSpeed
		if self.rect.right < 0:
			self.moving = False

	def setEnemy(self, top, left, speed):
		self.moving = True
		self.rect.top = top
		self.rect.left = left
		self.moveSpeed = speed
