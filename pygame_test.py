import pygame					# importer la bibliothèque
from pygame.locals import *		# importation des constantes

pygame.init()					# initialisation des modules

# DIMENSIONS DE LA FENETRE
fenetre = pygame.display.set_mode((640, 480))			# on peut ajouter RESIZABLE ou FULLSCREEN pour redimensionner le fentre ou l'afficher en plein écran

# CHARGEMENT DU FOND
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))								# image à coller et le point de collage

# CHARGEMENT DU PERSO
perso = pygame.image.load("perso.png").convert_alpha()	# La zone transparente est devenue noire -> convert_alpha()
position_perso = perso.get_rect()						# position du pero
fenetre.blit(perso, position_perso)
# perso.set_colorkey(perso, (0,0,0)) # pour rendre une couleur transparente mais ne fonctionne pas

# CHARGEMENT DE GUMBALL
gumball = pygame.image.load("gumball.png").convert_alpha()
gumball_x = 0
gumball_y = 0
fenetre.blit(gumball, (gumball_x, gumball_y))

# MAJ DE L'ECRAN
pygame.display.flip()
pygame.key.set_repeat(400, 30)

# BOUCLE INFINIE
continuer = 1
while continuer :
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0

		# MOUVEMENT GRACE AUX TOUCHES
		if event.type == KEYDOWN:						# pression d'une touche
			if event.key == K_SPACE:
				print("Espace")
			if event.key == K_RETURN:
				print("Entrée")
			if event.key == K_DELETE:
				continuer = 0

			if event.key == K_DOWN:
				position_perso = position_perso.move(0, 3)
			if event.key == K_RIGHT:
				position_perso = position_perso.move(3, 0)
			if event.key == K_UP:
				position_perso = position_perso.move(0, -3)
			if event.key == K_LEFT:
				position_perso = position_perso.move(-3, 0)

		# EVENEMENTS AVEC LA SOURIS
		"""if event.type == MOUSEBUTTONDOWN:
			if event.button == 1:
				gumball_x = event.pos[0]
				gumball_y = event.pos[1]"""
		# gumball se deplace ou l'on clique

		# SUIVI DE LA SOURIS
		if event.type == MOUSEMOTION:
			gumball_x = event.pos[0]
			gumball_y = event.pos[1]



	fenetre.blit(fond, (0,0))
	fenetre.blit(perso, position_perso)
	fenetre.blit(gumball, (gumball_x, gumball_y))
	pygame.display.flip()
