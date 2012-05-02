from Entity import Entity
from random import random

class Enemy(Entity):

	def __init__(self, image_paths, fps=10):
		Entity.__init__(self,image_paths,(-9001,-9001),fps,1)

	def update(self,t=0):
		Entity.update(self,t)
		if self.rect.right < 0:
			self.rect.left = 1024
			self.rect.top = 300*random()
			self.setSpeed(-8.0*random()-7.0,0.0)
		print self._speed

	def setEnemy(self, top, left, speed):
		self.rect.top = top
		self.rect.left = left
		self.setSpeed(speed,'x')
