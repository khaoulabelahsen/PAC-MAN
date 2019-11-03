"""Classe du labyrinthe"""

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
		# OUVERTURE DU FICHIER ET PARCOURT LIGNE PAR LIGNE
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

		# AFFICHAGE DU NIVEAU
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


	def liste_libres(self):
		"""Méthode permettant de lister les cases disponibles et accessibles par le Pac-Man"""
		libres = []
		num_ligne = 0
		for ligne in self.structure:
			num_case = 0
			for sprite in ligne:
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				# on ne considère pas les coudes ou les intersections
				if sprite == '0':
					libres.append([x, y])
				num_case += 1
			num_ligne += 1
		return libres
