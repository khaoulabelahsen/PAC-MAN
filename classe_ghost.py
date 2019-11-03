"""Classe des fantômes"""

import pygame
import random
from pygame.locals import *
from constantes import *

class Ghost:
	"""Classe permettant de créer et contrôler les fantômes du jeu"""
	def __init__(self, droite, gauche, haut, bas, niveau, sens):
		# CHARGEMENT DES IMAGES DU PERSO
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()

		# POSITION INITIALE EN CASES ET EN PIXELS
		[self.case_x, self.case_y] = random.choice([[12, 15], [15, 15]])
		self.x = self.case_x * taille_sprite
		self.y = self.case_y * taille_sprite

		# DIRECTION DU PERSO PAR DEFAUT
		self.direction = self.droite
		self.sens = 'haut'

		self.niveau = niveau


	def deplacer_continu(self, direction_continu, x, y, hunt, ghost, sens_pm, sens_ghost):
		"""
		Méthode permettant au fantôme de trouver sa direction avant de se déplacer selon sa position et celle de Pac-Man

		Paramètres :
		direction_continu : chaine de caractères ; direction qu'avait le fantôme à l'étape précédente
		x, y : entiers ; coordonnées en cases de la case à atteindre
		hunt : booléen ; True si le ghost est en chasse de PacMan, False sinon
		sens_pm : chaine de caractères ; direction de Pac-Man
		sens_ghost : chaine de caractères ; sens du fantôme

		Retour :
		direction_continu : chaine de caractères ; direction que doit prendre le fantôme
		"""

		# ON EST SUR UNE INTERSECTION : IL FAUT FAIRE UN CHOIX SELON NOTRE DIRECTION
		if self.niveau.structure[self.case_y][self.case_x] == 'i':
			choices = []
			# SI ON N'A PAS DE MUR A NOTRE DROITE ET QUE L'ON NE SE DIRIGE PAS VERS LA GAUCHE
			if self.niveau.structure[self.case_y][self.case_x+1] != 'm' and direction_continu != 'gauche':
				# ON POURRA ALLER À DROITE
				choices.append('droite')
			if self.niveau.structure[self.case_y][self.case_x-1] != 'm' and direction_continu != 'droite':
				choices.append('gauche')
			if self.niveau.structure[self.case_y+1][self.case_x] != 'm' and direction_continu != 'haut' and self.niveau.structure[self.case_y+1][self.case_x] != 'x':
				choices.append('bas')
			if self.niveau.structure[self.case_y-1][self.case_x] != 'm' and direction_continu != 'bas':
				choices.append('haut')

			# SI ON EST EN MODE CHASSE
			if hunt:
				choices = set(choices)
				# différence de comportement selon les personnages
				possible = self.chasse(x, y, ghost, sens_pm, sens_ghost)
				# on prend une direction commune aux possibilités offertes par l'intersection et celles de la chasse
				if choices & possible != set():
					direction_continu = random.sample(choices & possible, 1)[0]
				else:
					# si aucune n'est commune : au hasard
					direction_continu = random.sample(choices, 1)[0]

			# SINON : MODE ALÉATOIRE
			else:
				direction_continu = random.choice(choices)

		# SI ON EST DANS LE REPÈRE
		elif self.niveau.structure[self.case_y][self.case_x] == 'f':
			direction_continu = 'haut'

		# SI ON EST SUR UN COUDE
		elif self.niveau.structure[self.case_y][self.case_x] == 'c':
			if direction_continu == 'droite':
				# en allant à droite, on ne peut que tourner en haut ou en bas
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

		# SI ON EST AUX BORDS DES TUNNELS
		elif self.niveau.structure[self.case_y][self.case_x] == 'r':
			direction_continu = 'gauche'
		elif self.niveau.structure[self.case_y][self.case_x] == 'l':
			direction_continu = 'droite'

		return direction_continu


	def deplacer(self, direction_continu):
		"""
		Méthode permettant d'actualiser la position du ghost

		Paramètres :
		direction_continu : chaine de caractères ; direction qu'a le fantômes

		Retour :
		None ; modification en place
		"""

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


	def find(self, x, y):
		"""
		Méthode indiquant la direction à prendre par le fantome pour se rapprocher de la case cible

		Paramètres :
		x, y : entiers ; position de la case à atteindre

		Retour :
		possible : set() ; contient les directions intéressantes pour rejoindre cette cases
		"""

		# LA CASE EST À NOTRE DROITE
		if self.case_x < x:
			# LA CASE EST AU DESSUS
			if self.case_y > y:
				possible = ['droite', 'haut']
			else:
				possible = ['droite', 'bas']
		else:
			if self.case_y > y:
				possible = ['gauche', 'haut']
			else:
				possible = ['gauche', 'bas']

		return set(possible)


	def chasse(self, px, py, ghost, sens_pm, sens_ghost):
		"""
		Méthode régissant les différents comportements des fantômes

		Paramètres :
		px, py : entiers ; correspondent aux positions de la case à atteindre
		ghost : chaine de caractères ; nom du fantôme
		sens_pm : chaine de caractères ; la direction de Pac-Man
		sens_ghost chaine de caractères ; la direction du fantôme

		Retour :
		possible : set() ; contient les directions à prendre intéressantes pour le fantôme
		"""

		if ghost == 'blinky':
			# Blinky suit directement Pac-Man
			possible = self.find(px, py)
		if ghost == 'pinky':
			# Pinky se dirige vers l'avant de Pac-Man
			if sens_pm == 'droite':
				possible = self.find(px+4, py)
			if sens_pm == 'gauche':
				possible = self.find(px-4, py)
			if sens_pm == 'haut':
				possible = self.find(px, py-4)
			if sens_pm == 'bas':
				possible = self.find(px, py+4)
		if ghost == 'inky':
			# Inky prend de temps en temps la direction opposée de Pac-man, on modélise cela par un demi-tour aléatoire
			choix = random.randint(0,1)
			if sens_ghost == 'gauche':
				if choix == 0:
					possible = set('droite')
				else:
					possible = self.find(px, py)
			if sens_ghost == 'droite':
				if choix == 0:
					possible = set('gauche')
				else:
					possible = self.find(px, py)
			if sens_ghost == 'haut':
				if choix == 0:
					possible = set('bas')
				else:
					possible = self.find(px, py)
			if sens_ghost == 'bas':
				if choix == 0:
					possible = set('haut')
				else:
					possible = self.find(px, py)
		if ghost == 'clyde':
			possible = self.find(px, py)

		return possible


	def retour_zone(self):
		"""
		Méthode permettant de ramener les fantômes dans leur zone après la mort du Pac-Man)

		Paramètres :
		None

		Retour :
		None
		"""

		[self.case_x, self.case_y] = random.choice([[12, 15], [15, 15]])
		self.x = self.case_x * taille_sprite
		self.y = self.case_y * taille_sprite
		self.direction = self.droite
		self.sens = 'haut'
