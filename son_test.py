import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640, 480))
son = pygame.mixer.Sound("bruit.wav")

continuer = 1
joue = 0

while continuer:
	for event in pygame.event.get():
		if event.type == QUIT:
			continuer = 0

		# LE SON JOUE SI L'ON PRESSE ESPACE
		if event.type == KEYDOWN and event.key == K_SPACE and joue == 0:
			son.play()
			joue = 1

		# LE JEU SORT DE PAUSE SI ON APPUIE SUR ESPACE
		if event.type == KEYDOWN and event.key == K_SPACE and joue == 1:
			pygame.mixer.unpause()

		# PAUSE SI ON LACHE ESPACE
		if event.type == KEYUP and event.key == K_SPACE and joue == 1:
			pygame.mixer.pause()

		# LE SON STOPPE SI ON PRESSE ENTREE
		if event.type == KEYDOWN and event.key == K_RETURN:
			son.stop()
			joue = 0
