#! /usr/bin/env python

# player class which inherits from entity
import entity

class Player(Entity):
	
	def __init__(self, filename):
		super(Player, self).__init__(filename)

