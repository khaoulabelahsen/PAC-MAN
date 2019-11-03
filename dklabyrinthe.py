#!/usr/bin/python3
#-*- coding: Utf-8 -*

"""
Jeu Donkey Kong Labyrinthe
Jeu dans lequel on doit déplacer DK jusqu'aux bananes à travers un labyrinthe.

Script Python
Fichiers : dklabyrinthe.py, classes.py, constantes.py, n1, n2 + images"""

import pygame
from pygame.locals import *

from classes import *
from constantes import *

pygame.init()

# FENETRE
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre))

# ICONE
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)

# TITRE
pygame.display.set_caption(titre_fenetre)

pygame.key.set_repeat(400, 30)

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
				# VARIABLE DU CHOIX DE NIVEAU
				choix = 0

			# CHOIS D'UN NIVEAU
			elif event.type == KEYDOWN:
				if event.key == K_F1:
					choix = 'n1'
					continuer_accueil = 0
				elif event.key == K_F2:
					choix = 'n2'
					continuer_accueil = 0

	# POUR EMPECHER DE CHARGER EN CAS DE QUIT
	if choix != 0:
		fond = pygame.image.load(image_fond).convert()
		niveau = Niveau(choix) # self = choix
		niveau.generer()
		niveau.afficher(fenetre)

		dk = Perso("images/dk_droite.png", "images/dk_gauche.png", "images/dk_haut.png", "images/dk_bas.png", niveau)

		# BOUCLE DE JEU
		while continuer_jeu:
			pygame.time.Clock().tick(30)

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

					elif event.key == K_RIGHT:
						dk.deplacer('droite')
					elif event.key == K_LEFT:
						dk.deplacer('gauche')
					elif event.key == K_UP:
						dk.deplacer('haut')
					elif event.key == K_DOWN:
						dk.deplacer('bas')

			# MISE A JOUR DES IMAGES
			fenetre.blit(fond, (0,0))
			niveau.afficher(fenetre)
			fenetre.blit(dk.direction, (dk.x, dk.y))
			pygame.display.flip()

			if niveau.structure[dk.case_y][dk.case_x] == 'a':
				continuer_jeu = 0
