# Ciclo típico juegos pygame

import pygame, sys

class Partida():
    runners=[]
    __lineaSalida = 20
    __lineaLlegada = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        self.__background = pygame.image.load("images/pistaHorizontal.png")
        pygame.display.set_caption("Carrera de bichos")
        

    def competir(self):
        gameOver = False
        while not gameOver:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    gameOver = True

            self.__screen.blit(self.__background,(0,0))
            pygame.display.flip()
        
        pygame.quit()
        sys.exit()
            


if __name__ == "__main__":
        miPartida = Partida()
        pygame.font.init()
        miPartida.competir()
        
        
    
    
    
    
# Lo mismo csin objetos
#ancho = 640
#alto = 480
#
#screen = pygame.display.set_mode((ancho, alto))
#screen.fill((255,0,0))
#pygame.display.set_caption("Ciclo básico pygame")
#
#pygame.init()
#

#pygame.quit()
#sys.exit()



