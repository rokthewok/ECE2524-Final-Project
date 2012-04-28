#! /usr/bin/env python

import pygame, sys
from pygame.locals import *
import player

# this contains the main loop of the game

def input(eventlist):
	"""simple function which provides some debugging capabilities
	   for the events gathered"""
	for event in eventlist:
		print event

pygame.init()
# initialize objects here
player = player.Player("dog.png")

window = pygame.display.set_mode((1024, 768))
pygame.display.set_caption('Go Dog, Go!')
screen = pygame.display.get_surface()

clock = pygame.time.Clock()

objects = pygame.sprite.RenderPlain((player))

while True:
	# catch event
	# respond to event
	# update objects
	clock.tick(60)
	elapsed_time = clock.get_time()
	#print elapsed_time

	event = pygame.event.poll()
	#print event	# for debugging purposes
	if event.type == QUIT:
		sys.exit(0)

	if event.type == KEYDOWN and event.key == K_UP:
		player.jumping = True

	screen.fill((0,0,0))
	# update and draw objects
	objects.update()
	objects.draw(screen)
	pygame.display.flip()
exit()

