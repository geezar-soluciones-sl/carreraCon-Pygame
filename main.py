# Ciclo típico juegos pygame

import pygame, sys, random

class Corredor():
    __listaDisfraces=("Player.png", "Player.png", "Player.png", "Player.png")

    
    
    def __init__(self, x=0, y=0, disfraz="Player.png"):
        self.disfraz= pygame.image.load("images/{}".format(disfraz))
        self.position = [x,y]
        self.name = "Jugador"
        
    def avanzar(self):
        avance = random.randint(1,6)
        self.position[0] += avance


class Partida():
    runners=[]
    __lineaSalida = 20
    __lineaLlegada = 620
    __listaPosIni = (80,160,240,320)
    __listaNombres = ("Angel", "Inge", "Ekhi", "Ras")
    
    def __init__(self):
#        self.runners=[]
        self.__screen = pygame.display.set_mode((640,480))
        self.__background = pygame.image.load("images/pistaHorizontal.png")
        pygame.display.set_caption("Carrera de bichos")
        
        for i in range(4):
            corredorCreado = Corredor(self.__lineaSalida, self.__listaPosIni[i])
            corredorCreado.name = self.__listaNombres[i]
            self.runners.append(corredorCreado)
    

    def competir(self):
        gameOver = False
        while not gameOver:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    gameOver = True
        
            for item in self.runners:
                  item.avanzar()
                  if item.position[0]>=self.__lineaLlegada:
                      print("{} ha ganado".format(item.name))
                      gameOver = True
        
            self.__screen.blit(self.__background,(0,0))
            for item in self.runners:
                self.__screen.blit(item.disfraz, item.position)
                      
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



