from Entity import Entity
from random import random

class Enemy(Entity):

	def __init__(self, image_paths, fps=10):
		Entity.__init__(self,image_paths,(0,0),fps,1)
		self.moveSpeed = 0
		self.x_vel = 0

	def update(self,t=0):
		Entity.update(self,t)
		self.rect.left += self.moveSpeed
		if self.rect.right < 0:
			self.rect.left = 1024
			self.rect.top = 300*random()
			self.moveSpeed = -5*random()-1

	def setEnemy(self, top, left, speed):
		self.moving = True
		self.rect.top = top
		self.rect.left = left
		self.moveSpeed = speed
