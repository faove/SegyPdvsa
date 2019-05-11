import pygame

import sys

from pygame.locals import *

pygame.init()

# Definimos el color de fondo y el de la diagonal 

COLOR_FONDO = (150, 150, 200)

COLOR_LINEA1 = (255, 0, 0)

COLOR_LINEA2 = (0, 0, 255)

pantalla = pygame.display.set_mode((800,600))

refresco = pygame.time.Clock()

while True: time_passed = refresco.tick(30)

for event in pygame.event.get():
    if event.type == QUIT:
        sys.exit()

pantalla.fill(COLOR_FONDO)
pygame.draw.circle(pantalla, COLOR_LINEA1, (1, 1), (799, 599))

pygame.draw.aaline(pantalla, COLOR_LINEA2, (799, 1), (1, 599))

pygame.display.flip()

    
    