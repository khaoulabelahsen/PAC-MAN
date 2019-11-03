"""Classes du jeu PacMan"""

import pygame
import random
from pygame.locals import *
from constantes import *

class Niveau:
	"""Classe permettant de créer un niveau"""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0

	def generer(self):
		"""Méthode permettant de générer le niveau en fonction du fichier"""
		# OUVERTURE DU FICHIER
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			for ligne in fichier:
				ligne_niveau = []
				for sprite in ligne:
					if sprite != '\n':
						ligne_niveau.append(sprite)
				structure_niveau.append(ligne_niveau)
			self.structure = structure_niveau
		return structure_niveau

	def afficher(self, fenetre):
		"""Méthode permettant d'afficher le niveau en fonction de la liste de structure renvoyée par generer()"""

		# CHARGEMENT DES IMAGES
		mur = pygame.image.load(image_mur).convert()
		entree = pygame.image.load(image_entree).convert()

		# CREATION DU NIVEAU
		num_ligne = 0
		for ligne in self.structure:
			num_case = 0
			for sprite in ligne:
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == 'm':
					fenetre.blit(mur, (x, y))
				elif sprite == 'x':
					fenetre.blit(entree, (x, y))
				num_case += 1
			num_ligne += 1

class Perso:
	"""Classe permettant de créer un personnage"""

	def __init__(self, droite, gauche, haut, bas, niveau, sens):
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()

		# POSITION EN CASES ET EN PIXELS
		self.case_x = 13
		self.case_y = 23
		self.x = 13 * taille_sprite
		self.y = 23 * taille_sprite

		# DIRECTION DU PERSO PAR DEFAUT
		self.direction = self.droite
		self.niveau = niveau
		self.sens = "droite"

	def deplacement(self, direction):
		# SI ON NE PEUT PAS ALLER DANS CETTE DIRECTION, ON GARDE L'ANCIENNE
		if self.possible(direction) == 0:
			self.change_positions(self.sens)
		else:
			self.change_positions(direction)
			self.sens = direction

	def possible(self, direction):
		"""Méthode permettant de savoir si le PacMan peut se déplacer"""
		if direction == "gauche":
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
					return 1
				else:
					return 0
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
		"""Méthode permettant de changer la position du PacMan selon la direction demandée"""
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
			# POUR NE PAS SORTIR DE L'ECRAN
			if self.case_x > 0:
				# ON NE FONCE PAS DANS UN MUR
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
			elif self.case_y == 14:
				self.case_x = 27
				self.x = self.case_x * taille_sprite
			self.direction = self.gauche

		if direction == 'haut':
			# POUR NE PAS SORTIR DE L'ECRAN
			if self.case_y > 0:
				# ON NE FONCE PAS DANS UN MUR
				if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
			self.direction = self.haut

		if direction == 'bas':
			# POUR NE PAS SORTIR DE L'ECRAN
			if self.case_y < nombre_sprite_hauteur - 1:
				# ON NE FONCE PAS DANS UN MUR NI DANS LE DOMAINE DES FANTOMES
				if self.niveau.structure[self.case_y+1][self.case_x] != 'm' and self.niveau.structure[self.case_y+1][self.case_x] != 'x':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.bas

class Ghost:
	def __init__(self, droite, gauche, haut, bas, niveau):
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()

		# POSITION EN CASES ET EN PIXELS
		self.case_x = 14
		self.case_y = 11
		self.x = 14 * taille_sprite
		self.y = 11 * taille_sprite

		# DIRECTION DU PERSO PAR DEFAUT
		self.direction = self.droite
		self.niveau = niveau

	def deplacer_continu(self, direction_continu):
		"""Méthode de la classe Ghost2 permettant au fantome de trouver sa direction avant de se déplacer selon sa position et celle de PacMan"""

		# ON EST SUR UNE INTERSECTION : IL FAUT FAIRE UN CHOIX SELON NOTRE DIRECTION
		if self.niveau.structure[self.case_y][self.case_x] == 'i':
			choices = []
			# SI ON N'A PAS DE MUR A NOTRE DROITE ET QUE L'ON NE SE DIRIGE PAS VERS LA GAUCHE
			if self.niveau.structure[self.case_y][self.case_x+1] != 'm' and direction_continu != 'gauche':
				# ON POURRA ALLER À DROITE
				choices.append('droite')
			if self.niveau.structure[self.case_y][self.case_x-1] != 'm' and direction_continu != 'droite':
				choices.append('gauche')
			if self.niveau.structure[self.case_y+1][self.case_x] != 'm' and direction_continu != 'haut' :
				choices.append('bas')
			if self.niveau.structure[self.case_y-1][self.case_x] != 'm' and direction_continu != 'bas':
				choices.append('haut')

			direction_continu = random.choice(choices)

		# SI ON EST SUR UN COUDE
		elif self.niveau.structure[self.case_y][self.case_x] == 'c':
			if direction_continu == 'droite':
				if self.niveau.structure[self.case_y-1][self.case_x] == '0':
					direction_continu = 'haut'
				else:
					direction_continu = 'bas'
			elif direction_continu == 'gauche':
				if self.niveau.structure[self.case_y-1][self.case_x] == '0':
					direction_continu = 'haut'
				else:
					direction_continu = 'bas'
			elif direction_continu == 'haut':
				if self.niveau.structure[self.case_y][self.case_x+1] == '0':
					direction_continu = 'droite'
				else:
					direction_continu = 'gauche'
			else:
				if self.niveau.structure[self.case_y][self.case_x+1] == '0':
					direction_continu = 'droite'
				else:
					direction_continu = 'gauche'

		elif self.niveau.structure[self.case_y][self.case_x] == 'r':
			direction_continu = 'gauche'
		elif self.niveau.structure[self.case_y][self.case_x] == 'l':
			direction_continu = 'droite'

		return direction_continu

	def deplacer(self, direction_continu):
		if direction_continu == 'gauche':
			if self.case_x > 0:
				self.case_x -= 1
			elif self.case_y == 14:
				self.case_x = 27
			self.x = self.case_x * taille_sprite
			self.direction = self.gauche
		elif direction_continu == 'droite':
			if self.case_x < nombre_sprite_largeur - 1:
				self.case_x += 1
			elif self.case_y == 14:
				self.case_x = 0
			self.x = self.case_x * taille_sprite
			self.direction = self.droite
		elif direction_continu == 'haut':
			self.case_y -= 1
			self.y = self.case_y * taille_sprite
			self.direction = self.haut
		else:
			self.case_y += 1
			self.y = self.case_y * taille_sprite
			self.direction = self.bas

class Gums:
	"""Classe permettant d'intégrer les Pac-Gums."""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0

	def create(self):
		"""Méthode permettant de générer la matrice des gommes en fonction du fichier"""
		with open(self.fichier, "r") as fichier:
			matrice = []
			for ligne in fichier:
				ligne_matrice = []
				for element in ligne:
					if element != "\n":
						if element == "0" or element == "i" or element == "c":
							ligne_matrice.append("b")
						else:
							ligne_matrice.append("o")
				matrice.append(ligne_matrice)
			self.structure = matrice
		return matrice

	def afficher_gums(self, fenetre):
		"""Méthode permettant d'afficher les gums en fonction de la structure matrice renvoyée par create()"""
		gum = pygame.image.load(image_gum).convert_alpha()

		num_ligne = 0
		for ligne in self.structure:
			num_case =0
			for element in ligne:
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if element == 'b':
					fenetre.blit(gum, (x, y))
				num_case += 1
			num_ligne += 1

	def maj_gums(self, matrice):
		"""Méthode permettant de mettre à jour la carte des pac-gums en fonction de ceux déjà consommés par PacMan"""
		self.structure = matrice
		return self.structure

	def is_over(self, matrice):
		"""Méthode permettant de savoir s'il reste des pac-gums à récupérer"""
		over = 1
		for ligne in matrice:
			for element in ligne:
				# il reste des pacgums
				if element == "b":
					return 0
		return over
