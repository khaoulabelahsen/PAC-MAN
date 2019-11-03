"""d = sprite de depart
a = sprite d arrivée
m = sprite de mur
0 = mur"""

"""Classes du jeu Donkey Kong Labyrinthe"""

import pygame
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

	def afficher(self, fenetre):
		"""Méthode permettant d'afficher le niveau en fonction de la liste de structure renvoyée par generer()"""

		# CHARGEMENT DES IMAGES
		
		mur = pygame.image.load(image_mur).convert()
		depart = pygame.image.load(image_depart).convert()
		arrivee = pygame.image.load(image_arrivee).convert_alpha()

		# CREATION DU NIVEAU
		num_ligne = 0
		for ligne in self.structure:
			num_case = 0
			for sprite in ligne:
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == 'm':
					fenetre.blit(mur, (x, y))
				elif sprite == 'd':
					fenetre.blit(depart, (x, y))
				elif sprite == 'a':
					fenetre.blit(arrivee, (x, y))
				num_case += 1
			num_ligne += 1

class Perso:
	"""Classe permettant de créer un personnage"""

	def __init__(self, droite, gauche, haut, bas, niveau):
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()

		# POSITION EN CASES ET EN PIXELS
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0

		# DIRECTION DU PERSO PAR DEFAUT
		self.direction = self.droite
		self.niveau = niveau

	def deplacer(self, direction):
		"""Methode permettant de deplacer le personnage"""

		# DEPLACEMENT VERS LA DROITE
		if direction == 'droite':
			# POUR NE PAS SORTIR DE L'ECRAN
			if self.case_x < nombre_sprite_cote - 1:
				# ON NE FONCE PAS DANS UN MUR
				if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
					self.case_x += 1
					self.x = self.case_x * taille_sprite
			self.direction = self.droite

		# DEPLACEMENT VERS LA GAUCHE
		if direction == 'gauche':
			# POUR NE PAS SORTIR DE L'ECRAN
			if self.case_x > 0:
				# ON NE FONCE PAS DANS UN MUR
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
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
			if self.case_y < nombre_sprite_cote-1:
				# ON NE FONCE PAS DANS UN MUR
				if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.bas
