import pygame

pygame.display.set_mode((320,500))

logo = pygame.image.load("pacman.jpg")

fondo = pygame.image.load("fondopac-man-2.jpg")

posy = 100
##while True:
##    posx = posx + 1
##    
####    time_passed = pygame.time.Clock().tick(30)
##    for event in pygame.event.get():
##
##        if event.type == QUIT:
##
##            raise SystemExit
screen.blit(logo,(0,0))
##if screen.SPACE == True:
##    raise SystemExit
##    pygame.display.flip()