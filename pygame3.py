# -*- coding: utf-8 –*-

# Importamos las librería de Pygame y las del sistema, necesarias para forzar el cierre

import pygame 

from pygame.locals import *

# Inicializamos

pygame.display.set_caption('Pac Man faove')

pygame.init()

# Definimos el color de fondo y el de las figuras

COLOR_FONDO = (0, 0, 0)

COLOR_CUADRADO = (255, 0, 0)

COLOR_CIRCULO = (0, 0, 255)

# Cargamos la imagen y hacemos transparente el fondo (antes verde)

logo = pygame.image.load("pacman.jpg")

letras = pygame.image.load("letraspacman.jpg")

##imagen_nave = pygame.image.load('folder.png')
##
##imagen_nave.set_colorkey((0, 255, 0))

# Definimos el tamaño de la aplicación y la tasa de refresco

pantalla = pygame.display.set_mode((800, 600))

posx = 0

posy =100

while True:
    
    posx = posx + 1
    
    time_passed = pygame.time.Clock().tick(30)

    # Comprobamos el cierre de la aplicación y en caso afirmativo lanzamos la función salir

    for event in pygame.event.get():
        
        teclas = pygame.key.get_pressed()
        
        if event.type == QUIT:

            raise SystemExit
        
        
##        simple_image = pygame.image.load('pacman.jpg')
##        
##        background = screen.convert()
##        
##        background.fill((200, 200, 200))


        # Fijamos el color de fondo y dibujamos las figuras y la imagen
##        screen.blit(fondo,(0,0))
        
        pantalla.fill(COLOR_FONDO)

        pygame.draw.rect(pantalla, COLOR_CUADRADO, (50, 50, 50, 50))

        pygame.draw.circle(pantalla, COLOR_CIRCULO, (400, 300), 15 )
        
        pantalla.blit(logo, (posx, posy))
        
        if teclas[K_LEFT]: 
               
            posy = posy - 5
            
            pantalla.blit(logo, (posx, posy))
            
        elif teclas[K_RIGHT]:
            
            posy = posy + 5
            
            pantalla.blit(logo, (posx, posy))
            
        pantalla.blit(letras, (0, 0))
        # Actualizamos la pantalla

        pygame.display.flip()
