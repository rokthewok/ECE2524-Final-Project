import pygame, sys
from pygame.locals import *

def GameOver(screen):
	running = True
	image = pygame.image.load( "gameover.png" )
	rect = image.get_rect()

	while running:
		
