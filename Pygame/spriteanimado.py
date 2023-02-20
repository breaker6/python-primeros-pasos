#Importamos la librería de pygame y sys que nos permitirá cerrar la ventana
import random
import pygame, sys
#Iniciamos pygame
pygame.init()

#Definimos los colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (800, 500)
screen = pygame.display.set_mode(size)
#Clock nos permitirá controlar los FPS del juego
clock = pygame.time.Clock()

#Creamos la clase del sprite del personaje
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.images = []
        #self.image = pygame.image.load("Pygame/images/tifa/battle_position/tifa-sprite-0000-right.png").convert()
        self.images.append(pygame.image.load("Pygame/images/tifa/battle_position/prueba/tifa-sprite-0000.jpg").convert())
        self.images.append(pygame.image.load("Pygame/images/tifa/battle_position/prueba/tifa-sprite-0001.jpg").convert())
        self.images.append(pygame.image.load("Pygame/images/tifa/battle_position/prueba/tifa-sprite-0002.jpg").convert())
        self.images.append(pygame.image.load("Pygame/images/tifa/battle_position/prueba/tifa-sprite-0003.jpg").convert())

        #self.images.set_colorkey(BLACK)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        #Marcamos las coordenadas iniciales y lo dibujamos en ellas
        coord_x = 10
        coord_y = 150
        self.rect.x = coord_x
        self.rect.y = coord_y
    #Cuando se ejecuta el update, revisará si tiene que mover el objeto o no
    #Para ello, usamos las variables globales x_speed y y_speed
    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        
        self.image = self.images[self.index]
        #self.rect.x += x_speed
        #self.rect.y += y_speed



item_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

player = Player()
all_sprite_list.add(player)

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
    #######Zona de dibujo
    #Rellenamos la pantalla con la imagen guardada en la posición que le decimos
    #screen.blit(background, [0, 0])
    #Dibujamos los sprites que tenemos en el grupo all_sprite_list
    all_sprite_list.draw(screen)
    #Ejecutamos el metodo update de los sprites. Esto hará que el personaje se mueva en función de si estamos pulsando
    player.update()

    #Actualizamos pantalla
    pygame.display.flip()
    #Definimos los FPS que se mueve
    clock.tick(20)