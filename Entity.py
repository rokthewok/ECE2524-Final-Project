import pygame

class Entity(pygame.sprite.Sprite):
	def __init__(self,image_path,initial_pos):
		#Call Sprite Constructor
		pygame.sprite.Sprite.__init__(self)
		#set image
		self.image = pygame.image.load(image_path)
		self.rect = self.image.get_rect()
		self.rect.topleft = initial_pos
