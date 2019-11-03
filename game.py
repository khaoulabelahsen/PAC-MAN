#!/usr/bin/python3
# -*- coding: Utf-8 -*

"""
Jeu Pac Man
Jeu dans lequel on doit déplacer Pac Man afin qu'il mange les pac gommes au travers d'un labyrinthe tout en évitant les fantômes ennemis.

Script Python
Fichiers : classe_pacman.py, classe_labyrinthe.py, classe_ghost.py, classe_gums.py, classe_bonus.py, constantes.py, level + images + sons
"""

import pygame
import time
import random
from pygame.locals import *

from classe_labyrinthe import *
from classe_pacman import *
from classe_ghost import *
from classe_bonus import *
from classe_gums import *
from constantes import *

# DÉMARRAGE DE PYGAME
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
rip = pygame.mixer.Sound(sound_death)

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
		# ON SYNCHRONISE LA BOUCLE AVEC UNE HORLOGE
		pygame.time.Clock().tick(30)

		for event in pygame.event.get():
			# SI ON QUITTE
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_DELETE:
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
		# CHARGEMENT DU FOND
		fond = pygame.image.load(image_fond).convert()
		niveau = Niveau(choix)
		niveau.generer()
		niveau.afficher(fenetre)
		gums = Gums(choix)
		gums.create()
		gums.afficher_gums(fenetre)
		matrice_gums = gums.create()

		# INITIALISATION DES VARIABLES DU JEU
		joue_intro = 0
		vies = 3
		score = 0
		score2 = 0
		tic = time.time()
		hunt = False
		libres = niveau.liste_libres()
		bonus_test = False
		dead = False
		k = 1

		# PERSONNAGES
		pm = Perso(image_droite, image_gauche, image_haut, image_bas, niveau, "droite")
		blinky = Ghost(red_droite, red_gauche, red_haut, red_bas, niveau, 'haut')
		clyde = Ghost(four_droite, four_gauche, four_haut, four_bas, niveau, 'haut')
		inky = Ghost(blue_droite, blue_gauche, blue_haut, blue_bas, niveau, 'haut')
		pinky = Ghost(pink_droite, pink_gauche, pink_haut, pink_bas, niveau, 'haut')
		bonus = Bonus(choix, image_cherry, image_straw, image_orange, image_galaxian)
		# premier mouvement
		blinky1, clyde1, inky1, pinky1 = 'haut', 'haut', 'haut', 'haut'
		bouger = "droite"

		# BOUCLE DE JEU
		while continuer_jeu:
			pygame.time.Clock().tick(8)

			# GESTION DU SON
			if joue_intro == 0:
				intro.play()
				joue_intro = 1
			if pygame.mixer.get_busy() == False:
				joue_intro = 0

			# INTERACTIONS UTILISATEUR-CLAVIER
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

					# MOUVEMENT DU PACMAN
					if event.key == K_RIGHT:
						bouger = "droite"
					elif event.key == K_LEFT:
						bouger = "gauche"
					elif event.key == K_UP:
						bouger = "haut"
					elif event.key == K_DOWN:
						bouger = "bas"

			# LAPS DE TEMPS AVANT DE REVIVRE
			if dead:
				time.sleep(2.5)
				dead = False

			# MOUVEMENT DU FANTOME
			# lancement du mode chasse
			toc = time.time()
			if toc - tic > 20 and hunt == True:
				hunt = False
				tic = time.time()
			if toc - tic > 7 and hunt == False:
				hunt = True
				tic = time.time()

			# déplacements des fantômes
			blinky1 = blinky.deplacer_continu(blinky1, pm.case_x, pm.case_y, hunt, 'blinky', pm.sens, blinky.sens)
			blinky.deplacer(blinky1)
			inky1 = inky.deplacer_continu(inky1, pm.case_x, pm.case_y, hunt, 'inky', pm.sens, inky.sens)
			inky.deplacer(inky1)
			pinky1 = pinky.deplacer_continu(pinky1, pm.case_x, pm.case_y, hunt, 'pinky', pm.sens, pinky.sens)
			pinky.deplacer(pinky1)
			clyde1 = clyde.deplacer_continu(clyde1, pm.case_x, pm.case_y, hunt, 'clyde', pm.sens, clyde.sens)
			clyde.deplacer(clyde1)

			# DÉPLACEMENT DU PAC-MAN
			pm.deplacement(bouger)

			# BONUS
			if bonus_test == False:
				# il n'y a pas de bonus sur la map : on en tire un
				[objet_bonus, fruit] = bonus.tirage_bonus()
				# si on en a tiré un
				if objet_bonus != 'nope':
					# on le place sur une case libre
					bonus_position = random.choice(libres)
					bonus_test = True

			# ACTUALISATION DU SCORE
			# si on se trouve sur une Pac-Gomme
			if matrice_gums[pm.case_y][pm.case_x] == "b":
				score2 += 10
				matrice_gums[pm.case_y][pm.case_x] = "o"
			if objet_bonus != 'nope':
				# si on se trouve sur un bonus qui existe
				if [20*pm.case_x, 20*pm.case_y] == bonus_position:
					score2 += bonus.points(fruit)
					objet_bonus = 'nope'
					bonus_test = False
			# si le score a augmenté
			if score2 != score:
				print("Score : ", score2)
				if score < k*1000 <= score2:
					vies += 1
					k += 1
					print("Vie supplémentaire !")
					print("Vies : ", vies)
				score = score2

			# TEST DE FIN DE JEU : PLUS AUCUN PAC-GOMME OU PLUS DE VIE
			if gums.is_over(matrice_gums) == 1:
				print("Congrats! You won the game!")
				continuer_jeu = 0
			if (pm.case_x == blinky.case_x and pm.case_y == blinky.case_y) or (pm.case_x == inky.case_x and pm.case_y == inky.case_y) or (pm.case_x == pinky.case_x and pm.case_y == pinky.case_y)\
			 or (pm.case_x == clyde.case_x and pm.case_y == clyde.case_y):
				vies = vies - 1
				rip.play()
				# les persos sont ramenés à leur case départ
				pm.retour_depart()
				blinky.retour_zone()
				pinky.retour_zone()
				inky.retour_zone()
				clyde.retour_zone()
				print("Vies : ", vies)
				dead = True
				if vies == 0:
					print("You lost, so bad :(")
					continuer_jeu = 0

			# MISE A JOUR DES IMAGES
			fenetre.blit(fond, (0,0))
			niveau.afficher(fenetre)
			fenetre.blit(pm.direction, (pm.x, pm.y))
			gums.maj_gums(matrice_gums)
			gums.afficher_gums(fenetre)
			fenetre.blit(blinky.direction, (blinky.x, blinky.y))
			fenetre.blit(inky.direction, (inky.x, inky.y))
			fenetre.blit(pinky.direction, (pinky.x, pinky.y))
			fenetre.blit(clyde.direction, (clyde.x, clyde.y))
			if objet_bonus != 'nope':
				fenetre.blit(objet_bonus, bonus_position)
			pygame.display.flip()
