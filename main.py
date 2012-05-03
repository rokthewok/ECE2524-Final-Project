#! /usr/bin/env python

import pygame, sys
from pygame.locals import *
import player
import enemy
import level
import Entity
import menu
from random import random
# this contains the main loop of the game

NUM_ENEMIES = 5

pygame.init()
# initialize objects here
level_one = level.Level("Images//background.png","Images//midground.png","Audio//level_one_music.wav")
player = player.Player(("Images//dog_cape1.png", "Images//dog_cape2.png"),3)

main_menu = menu.Menu( "Images//main_menu.png", "Audio//main_theme.wav" )
pause_menu = menu.PauseMenu( "Images//pausemenu.png" )

window = pygame.display.set_mode((1024, 384))
pygame.display.set_caption('Go Dog, Go!')
screen = pygame.display.get_surface()

clock = pygame.time.Clock()

enemies = []
for i in range(0,NUM_ENEMIES):
	enemies.append(enemy.Enemy(("Images//birdfly.png", "Images//birdglide.png"),3))

allsprites = pygame.sprite.OrderedUpdates((player,enemies))

# open the starting menu
main_menu.menu(screen)
# once the main menu is exited, start the level music THIS SHOULD BE ALTERED so we can load any level's music at a given time
level_one.start_music()
score = 0

while True:
	# catch event
	# respond to event
	# update objects
	elapsed_time = clock.tick(60)
	#print elapsed_time
	
	for guy in enemies:
		if pygame.sprite.collide_rect( player, guy ):
			player.takeDamage()
			#print "Health: %d" % player.getHealth() # test purposes
		if player.getHealth() == 0:
			# gameover.gameOver()
			pass

	event = pygame.event.poll()
	#print event	# for debugging purposes
	if event.type == QUIT:
		sys.exit(0)

	if event.type == KEYDOWN:
		if event.key == K_UP:
			player.jump()
		if event.key == K_ESCAPE:
			pause_menu.menu(screen)
		if event.key == K_b:
			test.setAnim(0,test._endFrame%4+1)
			print "test._startFrame=",test._startFrame," test._endFrame=",test._endFrame

	screen.fill((0,0,0))
	# update and draw objects

	#test.update(time_passed_seconds)
	level_one.update()
	level_one.draw(screen)

	allsprites.update(elapsed_time)
	allsprites.draw(screen)
	
	score += 1

	pygame.display.flip()
exit()

