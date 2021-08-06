import pygame
from pygame.locals import*
import time
import sys

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((600, 75))
pygame.display.set_caption("Engie import")
font = pygame.font.SysFont('Calibri', 25, True, False)
text = font.render("Pressez ESCAPE pour le commencer, ESC pour l'annuler", True, WHITE)
screen.blit(text, [0, 0])

pygame.display.update()

# waint until user quits
while True:
    pygame.event.wait()        

