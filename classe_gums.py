"""Classe des Pac-Gommes"""

import pygame
import random
from pygame.locals import *
from constantes import *

class Gums:
	"""Classe permettant d'intégrer les Pac-Gums."""

	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0

	def create(self):
		"""
		Méthode permettant de générer la matrice des gommes en fonction du fichier

		Paramètres :
		None

		Retour :
		matrice : liste de listes ; matrice contenant les emplacements des Pac-Gommes
		"""

		# on lit le fichier ligne par ligne
		with open(self.fichier, "r") as fichier:
			matrice = []
			for ligne in fichier:
				ligne_matrice = []
				for element in ligne:
					if element != "\n":
						# si c'est une case pratiquable, il y a une Pac-Gomme
						if element == "0" or element == "i" or element == "c":
							ligne_matrice.append("b")
						else:
							ligne_matrice.append("o")
				matrice.append(ligne_matrice)
			# on actualise la structure
			self.structure = matrice
		return matrice


	def afficher_gums(self, fenetre):
		"""
		Méthode permettant d'afficher les gums en fonction de la structure matrice renvoyée par create()

		Paramètres :
		fenetre

		Retour :
		None ; affichage des images sur place
		"""

		# chargement de l'image
		gum = pygame.image.load(image_gum).convert_alpha()
		num_ligne = 0
		# on parcourt la structure pour trouver les Pac-Gommes
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
		"""
		Méthode permettant de mettre à jour la carte des pac-gums en fonction de ceux déjà consommés par Pac-Man

		Paramètres :
		matrice : liste de listes ; matrice des Pac-Gommes

		Retour :
		self.structure ; nouvelle structure actualisée
		"""

		self.structure = matrice
		return self.structure


	def is_over(self, matrice):
		"""
		Méthode permettant de savoir s'il reste des pac-gums à récupérer

		Paramètres :
		matrice : liste de listes ; matrice des Pac-Gommes présentes

		Retour :
		over : entier ; vaut 0 s'il reste de Pac-Gommes, 1 sinon
		"""

		over = 1
		for ligne in matrice:
			for element in ligne:
				# il reste des pacgums
				if element == "b":
					return 0
		return over
