"""Classe des bonus"""

import pygame
import random
from pygame.locals import *
from constantes import *

class Bonus:
	"""Classe permettant de concevoir des bonus"""
	def __init__(self, fichier, cherry, straw, orange, galaxian):
		self.fichier = fichier
		self.liste = 0
		self.cherry = pygame.image.load(image_cherry).convert_alpha()
		self.galaxian = pygame.image.load(image_galaxian).convert_alpha()
		self.orange = pygame.image.load(image_orange).convert_alpha()
		self.straw = pygame.image.load(image_straw).convert_alpha()

	def tirage_bonus(self):
		"""Méthode permettant de placer aléatoirement un bonus sur la carte"""
		p = random.uniform(0,1)
		q1, q2, q3, q4, q5 = 0.2, 0.05, 0.04, 0.01, 0.7
		if p <= q1:
			return [self.cherry, 'cherry']
		elif q1 < p <= q1 + q2:
			return [self.straw, 'straw']
		elif q2 + q1 < p <= q1 + q2 + q3:
			return [self.orange, 'orange']
		elif q1 + q2 + q3 < p <= q1 + q2 + q3 + q4:
			return [self.galaxian, 'galaxian']
		else:
			return ['nope', 'nope']

	def points(self, fruit):
		"""
		Méthode renvoyant le nombre de points en fonction du fruit consommé

		Paramètre :
		fruit : chaine de caractères ; nature du bonus
		"""

		if fruit == 'cherry':
			return 100
		elif fruit == 'straw':
			return 500
		elif fruit == 'orange':
			return 1000
		elif fruit == 'galaxian':
			return 5000
