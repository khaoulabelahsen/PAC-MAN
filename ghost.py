#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Pac Man
Jeu dans lequel on doit déplacer Pac Man afin qu'il mange les pac gommes au travers d'un labyrinthe.

Script Python
Fichiers : pacman.py, classes.py, constantes.py, level + images
"""

import pygame
import time
import random
from pygame.locals import *

from classes import *
from constantes import *

pygame.init()

# FENETRE
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))

# ICONE
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)

# TITRE
pygame.display.set_caption(titre_fenetre)

pygame.key.set_repeat(400, 250)

# SONS
intro = pygame.mixer.Sound(sound_game)

# BOUCLE PRINCIPALE
continuer = 1

while continuer:
	# CHARGEMENT DE L'ECRAN
	accueil = pygame.image.load(image_accueil).convert()
	fenetre.blit(accueil, (0,0))
	pygame.display.flip()


	continuer_jeu = 1
	continuer_accueil = 1

	while continuer_accueil:
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():
			# SI ON QUITTE
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_jeu = 0
				continuer = 0
				continuer_accueil = 0
				choix = 0

 			# CHOIX D'UN NIVEAU
			elif event.type == KEYDOWN and event.key == K_RETURN:
				choix = 'level'
				continuer_accueil = 0

	# POUR EMPECHER DE CHARGER EN CAS DE QUIT
	if choix != 0:
		fond = pygame.image.load(image_fond).convert()
		niveau = Niveau(choix)
		niveau.generer()
		niveau.afficher(fenetre)

		# INITIALISATION
		joue_intro = 0

		# PERSONNAGES
		red = Ghost(red_droite, red_gauche, red_haut, red_bas, niveau)
		red1 = random.choice(['gauche', 'droite'])

		# BOUCLE DE JEU
		while continuer_jeu:
			pygame.time.Clock().tick(8)
			if joue_intro == 0:
				intro.play()
				joue_intro = 1
			if pygame.mixer.get_busy() == False:
				joue_intro = 0

			# MOUVEMENT DU PACMAN
			for event in pygame.event.get():
				if event.type == QUIT:
					continuer_jeu = 0
					continuer = 0

				elif event.type == KEYDOWN:
					if event.key == K_DELETE:
						continuer_jeu = 0
						continuer = 0
					elif event.key == K_ESCAPE:
						continuer_jeu = 0

			# MOUVEMENT DU FANTOME
			red1 = red.deplacer_continu(red1)
			red.deplacer(red1)

			# MISE A JOUR DES IMAGES
			fenetre.blit(fond, (0,0))
			niveau.afficher(fenetre)
			fenetre.blit(red.direction, (red.x, red.y))
			pygame.display.flip()
