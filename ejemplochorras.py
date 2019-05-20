# Carrera de tortugas con pygame
# Hay dos cosas siempre fijas en una "partida" (while not gameover):
# Comprobar eventos y refrescar pantalla

import pygame, sys

class runner():
    

class Game():
    
    corredores=[]
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Carrera de bichos")
        
        self.background = pygame.image.load("images/pistaHorizontal.png")
        self.runner = pygame.image.load("images/Player.png")
        



# Siempre en pygame (o en cualquier juego), se comprueban eventos y se refresca pantalla
    def competir(self):
        
        gameOver = False
        x=0
        
        while not gameOver:
            # Comprobación eventos desde el "escuchador" de eventos de pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            #Refrescar pantalla
            self.__screen.blit(self.background, (0,0)) # Coordenadas de pygame como en URSOS
            self.__screen.blit(self.runner, (x, 240)) # Poner jugador en su sitio
            pygame.display.flip() # refresca
            
            x += 3
            if x >= 620:
                gameOver = True
        
        pygame.quit()
        sys.exit()
        

if __name__ == "__main__":
    pygame.init()
    g = Game()
    g.competir()

#class Circuito():
#    corredores = []
#    posStartY = (-30,-10,10,30)
#    coloresT = ("red", "blue", "green", "orange")
#
#    def __init__(self, ancho, alto):
#        self.__screen = turtle.Screen()
## Ponemos la pantalla de módulo turtle. La hacemos privada.
## o se podrían cambiar cosas a mitad de partida desde cualquier sitio fácilmente
## En Python siempre se puede con miCirc._Circuito__screen
#        self.__screen.setup(ancho,alto)
#        self.__screen.bgcolor("lightgray")
#        self.__lineaSalida = 20-ancho/2
#        self.__lineaLlegada = ancho/2 -20
#        
#        self.__crearCorredores()
#    
#    def __crearCorredores(self):
#        for i in range(4):
#            newTurtle = turtle.Turtle()
#            newTurtle.shape("turtle")
#            newTurtle.penup() #"Levanta el boli" para que no se vean las lineas
#            newTurtle.setpos(self.__lineaSalida, self.posStartY[i])
#            newTurtle.color(self.coloresT[i])
#            
#            self.corredores.append(newTurtle)
#            
#    def competir(self):
#        
#        hayGanador = False
#        while not hayGanador:
#            for tortuga in self.corredores:
#                avance = random.randint(1,6)
#                tortuga.forward(avance)
#                if tortuga.position()[0] >= self.__lineaLlegada:
#                    hayGanador=True
#                    print("La tortuga de color {} ha ganado".format(tortuga.color()[0]))
#
## Ejecutamos algo en __main__ para ver cómo va
#
#if __name__ == "__main__":
#    circuito=Circuito(640,480)
#    circuito.competir()
#    

        
    
    