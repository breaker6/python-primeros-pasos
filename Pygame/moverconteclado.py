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

#Coordenadas iniciales del cuadrado
coord_x = 10
coord_y = 10
#Velocidad
x_speed = 0
y_speed = 0

while True:
    #Registramos todos los eventos que ocurren con el For
    for event in pygame.event.get():
        #Si se pulsa en el boton exit de la ventana de pygame, la cerramos
        if event.type == pygame.QUIT:
            sys.exit()
        ###EVENTOS TECLADO
        #Detectamos cuando se aprieta una tecla
        if event.type == pygame.KEYDOWN:
            #Si la tecla pulsada es una de las flechas del teclado, dará velocidad al objeto
            if event.key == pygame.K_LEFT:
                x_speed = -3
            if event.key == pygame.K_RIGHT:
                x_speed = 3
            if event.key == pygame.K_UP:
                y_speed = -3
            if event.key == pygame.K_DOWN:
                y_speed = 3
        #Detectamos cuando se deja de apretar una tecla
        if event.type == pygame.KEYUP:
            #Le damos velocidad 0 para que deje de moverse
            if event.key == pygame.K_LEFT:
                x_speed = 0
            if event.key == pygame.K_RIGHT:
                x_speed = 0
            if event.key == pygame.K_UP:
                y_speed = 0
            if event.key == pygame.K_DOWN:
                y_speed = 0
        ####Fin EVENTOS TECLADO
    ####LÓGICA DEL JUEGO
   
    ####FIN LÓGICA DEL JUEGO
    #Poner color de fondo a la pantalla
    screen.fill(WHITE)
    #######Zona de dibujo
    #Añadimos a las coordenadas iniciales la velocidad definida por las pulsación de teclas
    coord_x += x_speed
    coord_y += y_speed
    #Movemos el cuadro en función de las coordenadas resultado de la posición mas la velocidad
    pygame.draw.rect(screen, RED, (coord_x, coord_y, 100, 100))
    #######Fin Zona de dibujo
    #Actualizamos pantalla
    pygame.display.flip()
    #Definimos los FPS que se mueve
    clock.tick(80)