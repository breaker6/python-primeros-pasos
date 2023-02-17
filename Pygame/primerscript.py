#Importamos la librería de pygame y sys que nos permitirá cerrar la ventana
import pygame, sys
#Iniciamos pygame
pygame.init()

#Definimos el tamaño de la ventana en la variable size y creamos la ventana
size = (800, 500)
screen = pygame.display.set_mode(size)

while True:
    #Registramos todos los eventos que ocurren con el For
    for event in pygame.event.get():
        #Si se pulsa en el boton exit de la ventana de pygame, la cerramos
        if event.type == pygame.QUIT:
            sys.exit()