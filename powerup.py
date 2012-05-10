from Entity import Entity
from random import random

class PowerUp(Entity):

	def __init__(self, image_paths, fps=10):
		Entity.__init__(self,image_paths,(-9001,-9001),fps,1)
		#variable to tell if power up is moving, true if not moving
		self.readyToGo = True

	#update moves the power up to the left
	def update(self, t=0):
		Entity.update(self,t)
		#if power up goes off left side of screen, setReady and send next random power up
		if self.rect.right < 0:
			self.setReady()

	#setReady gets the power up ready to begin moving
	def setReady(self):
		self.rect.left = 2048 + 1024*random()
		self.rect.top = 300*random()
		self.setSpeed(0.0,0.0)
		self.readyToGo = True

	#setGo tells power up to start moving, only one power up at a time
	def setGo(self):
		self.setSpeed(-7.0,0.0)
		self.readyToGo = False
