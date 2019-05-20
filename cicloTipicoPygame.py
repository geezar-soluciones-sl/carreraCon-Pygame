# Ciclo típico juegos pygame

import pygame, sys

ancho = 640
alto = 480

screen = pygame.display.set_mode((ancho, alto))
screen.fill((255,0,0))
pygame.display.set_caption("Ciclo básico pygame")

pygame.init()

# Montamos ciclo (pintar-eventos-modificar pantalla-pìntar ...)
gameOver = False
while not gameOver:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            gameOver = True
    pygame.display.flip()
pygame.quit()
sys.exit()



