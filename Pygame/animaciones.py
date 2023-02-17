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

#Definimos las coordenadas en las que iniciará
cord_x= 400
cord_y= 200
#Definimos la velociada a la que se moverá
speed_x= 3
speed_y= 3

while True:
    #Registramos todos los eventos que ocurren con el For
    for event in pygame.event.get():
        #Si se pulsa en el boton exit de la ventana de pygame, la cerramos
        if event.type == pygame.QUIT:
            sys.exit()
    ####LÓGICA DEL JUEGO
    #Comprobaremos si llega al límite. Si llega, invertiremos la velocidad
    #para que vaya al revés
    if (cord_x > 720 or cord_x < 0):
        speed_x *= -1
    if (cord_y > 320 or cord_y < 0):
        speed_y *= -1
    #Definimos la animación sumando a la coordenada la velocidad
    cord_x+=speed_x
    cord_y+=speed_y
    ####FIN LÓGICA DEL JUEGO
    #Poner color de fondo a la pantalla
    screen.fill(WHITE)
    #######Zona de dibujo
    #Desplazaremos el rectangulo en función de las coordenadas
    pygame.draw.rect(screen, RED, (cord_x, cord_y, 80, 80))
    #######Fin Zona de dibujo
    #Actualizamos pantalla
    pygame.display.flip()
    #Definimos los FPS que se mueve
    clock.tick(80)