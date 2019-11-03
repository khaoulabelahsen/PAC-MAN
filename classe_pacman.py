"""Classes du personnage jouable Pac-Man"""

import pygame
import random
from pygame.locals import *
from constantes import *

class Perso:
	"""Classe permettant de créer et contrôler le personnage de Pac-Man"""

	def __init__(self, droite, gauche, haut, bas, niveau, sens):
		# CHARGEMENT DES IMAGES DU PERSO
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()

		# POSITION INITIALE EN CASES ET EN PIXELS
		self.case_x = 13
		self.case_y = 23
		self.x = 13 * taille_sprite
		self.y = 23 * taille_sprite

		# DIRECTION DU PERSO PAR DEFAUT
		self.direction = self.droite
		self.sens = "droite"

		self.niveau = niveau


	def deplacement(self, direction):
		"""Méthode permettant d'actualiser la direction du Pac-Man

		Paramètres :
		direction : chaine de caractères ; direction du Pac-Man

		Retour :
		None ; modification sur place
		"""

		# SI ON NE PEUT PAS ALLER DANS CETTE DIRECTION, ON GARDE L'ANCIENNE
		if self.possible(direction) == 0:
			self.change_positions(self.sens)
		else:
			self.change_positions(direction)
			self.sens = direction


	def possible(self, direction):
		"""
		Méthode permettant de savoir si le PacMan peut se déplacer.

		Paramètres :
		direction : chaine de caractères ; direction du Pac-MAN

		Retour :
		entier ; 0 ou 1 selon la possibilité
		"""

		# SI ON VEUT TOURNER À GAUCHE
		if direction == "gauche":
			if self.case_x > 0:
				# est-ce qu'il y aun mur ?
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
					return 1
				else:
					return 0
			# c'est le tunnel
			elif self.case_y == 14:
				return 1

		if direction == "droite":
			if self.case_x < nombre_sprite_largeur - 1:
				if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
					return 1
				else:
					return 0
			elif self.case_y == 14:
				return 1

		if direction == "haut":
			if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
				return 1
			else:
				return 0

		if direction == "bas":
			if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
				return 1
			else:
				return 0


	def change_positions(self, direction):
		"""
		Méthode permettant de changer la position du PacMan selon la direction demandée

		Paramètres :
		direction : chaine de caractères ; direction demandée par l'utilisateur

		Retour :
		None ; modification sur place
		"""

		if direction == 'droite':
			# POUR NE PAS SORTIR DE L'ECRAN
			if self.case_x < nombre_sprite_largeur - 1:
				# ON NE FONCE PAS DANS UN MUR
				if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
					self.case_x += 1
					self.x = self.case_x * taille_sprite
			elif self.case_y == 14:
				self.case_x = 0
				self.x = self.case_x * taille_sprite
			self.direction = self.droite

		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			elif self.case_y == 14:
				self.case_x = 27
				self.x = self.case_x * taille_sprite
			self.direction = self.gauche

		if direction == 'haut':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
			self.direction = self.haut

		if direction == 'bas':
			if self.case_y < nombre_sprite_hauteur - 1:
				# ON NE FONCE PAS DANS UN MUR NI DANS LE DOMAINE DES FANTOMES
				if self.niveau.structure[self.case_y+1][self.case_x] != 'm' and self.niveau.structure[self.case_y+1][self.case_x] != 'x':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.bas


	def retour_depart(self):
		"""
		Méthode permettant de ramener le Pac-Man à sa case départ en cas de perte de vie

		Paramètres :
		None

		Retour :
		None
		"""

		self.case_x = 13
		self.case_y = 23
		self.x = 13 * taille_sprite
		self.y = 23 * taille_sprite
		self.direction = self.droite
		self.sens = "droite"
