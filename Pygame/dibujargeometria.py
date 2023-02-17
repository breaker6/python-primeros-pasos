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

while True:
    #Registramos todos los eventos que ocurren con el For
    for event in pygame.event.get():
        #Si se pulsa en el boton exit de la ventana de pygame, la cerramos
        if event.type == pygame.QUIT:
            sys.exit()
    #Poner color de fondo a la pantalla
    screen.fill(WHITE)
    #######Zona de dibujo
    #Dibujamos una linea en pantalla verde que vaya desde las dos posiciones
    #definidas y que tenga un grosor de 5
    pygame.draw.line(screen, GREEN, [0, 100], [100, 100], 5)


    #######Fin Zona de dibujo
    #Actualizamos pantalla
    pygame.display.flip()