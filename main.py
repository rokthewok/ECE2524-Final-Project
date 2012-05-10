#! /usr/bin/env python

import pygame, sys
from pygame.locals import *
import player, enemy, powerup, level, Entity, menu, statcounter
from random import random
from gamestate import GameState
# this contains the main loop of the game

NUM_ENEMIES = 5

pygame.init()
#==================================================================================================
# initialize objects here
level_one = level.Level("Images//background.png","Images//midground.png","Audio//level_one_music.wav")
player = player.Player(("Images//dog_cape1.png", "Images//dog_cape2.png"),3)

bonePowerUp = powerup.PowerUp(("Images//bone.png", "Images//bone.png"),3)
tennisBallPowerUp = powerup.PowerUp(("Images//tennisball.png", "Images//tennisball.png"),3)
currentPowerUp = 2*random()

main_menu = menu.Menu( "Images//main_menu.png", "Audio//main_theme.wav" )
pause_menu = menu.PauseMenu( "Images//pausemenu.png" )
gameover_menu = menu.GameOverMenu( "Images//gameovermenu.png" )

window = pygame.display.set_mode((1024, 384))
pygame.display.set_caption('Go Dog, Go!')
screen = pygame.display.get_surface()

clock = pygame.time.Clock()

stats = statcounter.StatCounter()
statsgroup = pygame.sprite.GroupSingle(stats)

state = GameState.MAINMENU
#==================================================================================================

# create a list of enemies; will change in future updates
enemies = []
for i in range(0,NUM_ENEMIES):
	enemies.append(enemy.Enemy(("Images//birdfly.png", "Images//birdglide.png"),3))

# create a group to update the sprites in order
allsprites = pygame.sprite.OrderedUpdates((player,enemies,bonePowerUp,tennisBallPowerUp))

while True:

	if state == GameState.MAINMENU:
		# open the starting menu
		main_menu.menu(screen)
		state = GameState.PLAYING

	if state == GameState.PLAYING:	
		# once the main menu is exited, start the level music 
		# NOTE: THIS SHOULD BE ALTERED so we can load any level's music at a given time
		level_one.start_music()

		#Reset the score before beginning
		stats.score = 0

		while state == GameState.PLAYING:
			# catch event
			# respond to event
			# update objects
			elapsed_time = clock.tick(60)
	
			for guy in enemies:
				if pygame.sprite.collide_rect( player, guy ):
					player.takeDamage()
					#print "Health: %d" % player.getHealth() # test purposes
					if player.getHealth() == 0:
						state = GameState.GAMEOVER

			if currentPowerUp < 1: #bonePowerUp
				if bonePowerUp.readyToGo == True:
					bonePowerUp.setGo()
				if pygame.sprite.collide_rect(player, bonePowerUp):
					player.healHealth()
					currentPowerUp = 2*random()
					bonePowerUp.setReady()
			elif currentPowerUp < 2: #tennisBallPowerUp
				if tennisBallPowerUp.readyToGo == True:
					tennisBallPowerUp.setGo()
				if pygame.sprite.collide_rect(player, tennisBallPowerUp):
					stats.score += 2500
					currentPowerUp = 2*random()
					tennisBallPowerUp.setReady()

			event = pygame.event.poll()
			#print event	# for debugging purposes
			if event.type == QUIT:
				sys.exit(0)

			if event.type == KEYDOWN:
				if event.key == K_UP or event.key == K_SPACE: #Jump button 
					player.jump()
				elif event.key == K_ESCAPE: #Pause button
					pause_menu.menu(screen,clock)
				elif event.key == K_LEFT: #Move left
					if player.rect.left > 0:
						player.moveHoriz(-15)
				elif event.key == K_RIGHT: #Move right
					if player.rect.right < 1024:
						player.moveHoriz(15)
				#if event.key == K_b: #old test code
					#test.setAnim(0,test._endFrame%4+1)
					#print "test._startFrame=",test._startFrame," test._endFrame=",test._endFrame

			# update and draw objects

			level_one.update()
			level_one.draw(screen)
	
			stats.update(player.getHealth(), elapsed_time)

			allsprites.update(elapsed_time)
			allsprites.draw(screen)
			statsgroup.draw(screen)

			pygame.display.flip()

	if state == GameState.GAMEOVER:
		decision = gameover_menu.menu(screen) #Returns whether to start over or quit
		if decision == True:
			player.resetHealth()
			state = GameState.MAINMENU
		else:
			sys.exit(0)

exit()

