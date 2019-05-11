# -*- coding: utf-8 –*-

import pygame 
from pygame.locals import *

pygame.init()

pygame.display.set_mode((200, 200))

pygame.display.flip()

event = pygame.event.poll()

while True:

    cursor = pygame.mouse.get_pos()

    evento = pygame.event.wait()

    if evento.type == QUIT or evento.type == K_ESCAPE:

        print "Has abandonado la aplicación"

        raise SystemExit

    if pygame.mouse.get_pressed()[0]:

        print "Has usado el botón izquierdo del ratón"

    if pygame.mouse.get_pressed()[1]:

        print "Has usado el botón central del ratón"

    if pygame.mouse.get_pressed()[2]:

        print "Has usado el botón derecho del ratón"

    if evento.type == KEYDOWN and evento.key == K_SPACE:

        print "Has pulsado espacio"

    if evento.type == KEYDOWN and evento.key == K_BACKSPACE:

        print "Has pulsado backspace"

