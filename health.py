from Entity import Entity

class Health(Entity):

	def __init__(self, image_path,fps = 10):
		self.lives = 3
		self.image_path = image_path
		#self.showLives()

	def update(self,t=0):
		Entity.update(self,t)
			
	def showLives(self):
		#for x in range(0, self.lives-1)
		#	Entity.__init__(self,image_paths,(300, 20), 10)				
		
