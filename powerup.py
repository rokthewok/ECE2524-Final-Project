from Entity import Entity
from random import random

class PowerUp(Entity):

	def __init__(self, image_paths, fps=10):
		Entity.__init__(self,image_paths,(-9001,-9001),fps,1)
		self.readyToGo = True

	def update(self, t=0):
		Entity.update(self,t)
		if self.rect.right < 0:
			self.setReady()

	def setReady(self):
		self.rect.left = 3072 + 1024*random()
		self.rect.top = 300*random()
		self.setSpeed(0.0,0.0)
		self.readyToGo = True

	def setGo(self):
		self.setSpeed(-7.0,0.0)
		self.readyToGo = False
