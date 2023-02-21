#Importamos la librería de pygame y sys que nos permitirá cerrar la ventana
import pygame, sys
#Iniciamos pygame
pygame.init()

#Definimos los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

#Definimos el tamaño de la ventana en la variable size y creamos la ventana
size = (800, 500)
screen = pygame.display.set_mode(size)
#Clock nos permitirá controlar los FPS del juego
clock = pygame.time.Clock()

#Cargamos la imagen en la variable background. El convert del final ayuda a pygame a procesar la imagen
background = pygame.image.load("Pygame/images/background.png").convert()
#Cargamos la imagen del personaje
character = pygame.image.load("Pygame/images/tifa/battle_position/tifa-sprite-0000.png").convert()
#Eliminamos el color de fondo de la imagen del personaje
character.set_colorkey([0, 0, 0])

while True:
    #Registramos todos los eventos que ocurren con el For
    for event in pygame.event.get():
        #Si se pulsa en el boton exit de la ventana de pygame, la cerramos
        if event.type == pygame.QUIT:
            sys.exit()
    ####LÓGICA DEL JUEGO
   

    ####FIN LÓGICA DEL JUEGO
    #######Zona de dibujo
    
    #Rellenamos la pantalla con la imagen guardada en la posición que le decimos
    screen.blit(background, [0, 0])
    #Cargamos la imagen del personaje
    screen.blit(character, [0, 100])
 
    #######Fin Zona de dibujo
    #Actualizamos pantalla
    pygame.display.flip()
    #Definimos los FPS que se mueve
    clock.tick(80)