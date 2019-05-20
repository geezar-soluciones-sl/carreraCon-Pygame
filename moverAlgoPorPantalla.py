# MOVIMIENTO DE BICHOS POR PANTALLA CON TECLAS
# Hay que importar pygame.locals

import pygame, sys, random
from pygame.locals import *

class Corredor():
#    __listaDisfraces=("Player.png", "Player.png", "Player.png", "Player.png") 
    
    def __init__(self, x=0, y=0, disfraz=None):
        disfraz = "Player.png"
        self.disfraz= pygame.image.load("images/{}".format(disfraz))
        self.position = [x,y]
        self.name = "Bichejo feo"
        

class Partida():
    
    def __init__(self):
# 
        self.__screen = pygame.display.set_mode((640,480))
        self.__background = pygame.image.load("images/pistaHorizontal.png")
        pygame.display.set_caption("Carrera de bichos")
        
        self.bicho = Corredor(320,240) # En medio
        
    def comienzo(self):
        gameOver = False
        while not gameOver:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif evento.type == KEYDOWN:      # Buscar eventos KEY y MOUSE en pygame.key
                    if evento.key == K_UP:
                        self.bicho.position[1] += -5
                    elif evento.key == K_DOWN:
                        self.bicho.position[1] += 5
                    elif evento.key == K_LEFT:
                        self.bicho.position[0] += -5
                    elif evento.key == K_RIGHT:
                        self.bicho.position[0] += 5
                    else:
                        pass
                    
            self.__screen.blit(self.__background,(0,0))
                
            self.__screen.blit(self.bicho.disfraz, self.bicho.position)
            
            pygame.display.flip()
                    

miPartida = Partida()
pygame.font.init()
miPartida.comienzo()
