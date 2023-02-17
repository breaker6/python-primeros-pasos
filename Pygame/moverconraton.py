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

#Ponemos la visibilidad del ratón en 0 para que no se vea
pygame.mouse.set_visible(0)

while True:
    #Registramos todos los eventos que ocurren con el For
    for event in pygame.event.get():
        #Si se pulsa en el boton exit de la ventana de pygame, la cerramos
        if event.type == pygame.QUIT:
            sys.exit()
    ####LÓGICA DEL JUEGO
    #Cogemos la posición del ratón. pygame.mouse.get_pos() nos la da en una tupla tipo (x, y)
    mouse_pos = pygame.mouse.get_pos()
    #Guardamos ambas posiciones en las variables x e y
    x = mouse_pos[0]
    y = mouse_pos[1]
    ####FIN LÓGICA DEL JUEGO
    #Poner color de fondo a la pantalla
    screen.fill(WHITE)
    #######Zona de dibujo
    #Dibujamos el rectangulo en la posición en la que está el ratón
    pygame.draw.rect(screen, RED, (x, y, 100, 100))
    #######Fin Zona de dibujo
    #Actualizamos pantalla
    pygame.display.flip()
    #Definimos los FPS que se mueve
    clock.tick(80)