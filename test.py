import pygame
from pygame.locals import *

#Initialisation
pygame.init()
fenetre = pygame.display.set_mode((300,300))
son = pygame.mixer.Sound("son.wav")

continuer = 1 #Variable de boucle
joue = 0 #1 si le son a été mis en pause

while continuer:
	for event in pygame.event.get():
        #Quitter
		if event.type == QUIT:
			continuer = 0

		#Lancer le son
		if event.type == KEYDOWN and event.key == K_SPACE and joue == 0:
			son.play()
			joue = 1
		#Sortir de pause
		if event.type == KEYDOWN and event.key == K_SPACE and joue == 1:
			pygame.mixer.unpause()
		#Mettre en pause
		if event.type == KEYUP and event.key == K_SPACE:
			pygame.mixer.pause()
		#Stopper
		if event.type == KEYDOWN and event.key == K_RETURN:
			son.stop()
			joue = 0
