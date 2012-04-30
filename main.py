#! /usr/bin/env python

import pygame, sys
from pygame.locals import *
import player
import level
import Entity
import menu
# this contains the main loop of the game

pygame.init()
# initialize objects here
#<<<<<<< HEAD
#player = player.Player("dog_cape1.png", "dog_cape2.png")
level_one = level.Level("Images//background.png","Images//midground.png","level_one_music.mp3")
test = Entity.Entity(("Images//dog_cape1.png","Images//dog_cape2.png"),[0,200],3)
#=======
player = player.Player(("Images//dog_cape1.png", "Images//dog_cape2.png"),3)

window = pygame.display.set_mode((1024, 384))
pygame.display.set_caption('Go Dog, Go!')
screen = pygame.display.get_surface()

clock = pygame.time.Clock()

objects = pygame.sprite.OrderedUpdates((player,test))

# open the starting menu
main_menu = menu.Menu( "Images//main_menu.png" )
main_menu.menu(screen)

while True:
	# catch event
	# respond to event
	# update objects
	elapsed_time = clock.tick(60)
	#print elapsed_time

	event = pygame.event.poll()
	#print event	# for debugging purposes
	if event.type == QUIT:
		sys.exit(0)

	if event.type == KEYDOWN:
		if event.key == K_UP:
			player.jumping = True
		if event.key == K_ESCAPE:
			sys.exit(0)

	screen.fill((0,0,0))
	# update and draw objects

	#test.update(time_passed_seconds)
	level_one.update()
	level_one.draw(screen)

	objects.update(elapsed_time)
	objects.draw(screen)
	pygame.display.flip()
exit()

