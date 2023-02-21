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
        #Cargamos todas las imagenes del sprite en el array self.images
        self.images = []
        self.images.append(pygame.image.load("Pygame/images/tifa/battle_position/tifa-sprite-0000.png").convert())
        self.images.append(pygame.image.load("Pygame/images/tifa/battle_position/tifa-sprite-0001.png").convert())
        self.images.append(pygame.image.load("Pygame/images/tifa/battle_position/tifa-sprite-0002.png").convert())
        self.images.append(pygame.image.load("Pygame/images/tifa/battle_position/tifa-sprite-0003.png").convert())

        #Iniciamos el indice que dirá en que fotograma estamos de la animación
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        #Marcamos las coordenadas iniciales
        coord_x = 10
        coord_y = 150
        #Pintamos el sprite
        self.rect.x = coord_x
        self.rect.y = coord_y
        #Variable para contar los FPS (Nos permitirá controlar la velocidad de la animación)
        self.countFPS = 0
        #Volteamos la imagen (Lo hacemos porque el sprite está mirando a la izquierda y queremos que mire a la derecha)
        self.image = pygame.transform.flip(self.images[self.index], True, False)
    #En el update controlaremos varias cosas
    def update(self):
        #Controlaremos los FPS con la variable countFPS. Eso nos permitirá controlar la velocidad de la animación
        self.countFPS += 1
        if self.countFPS >= 5:
            #Cuando llegamos al número de fotogramas escrito, aumentamos el indice de la animación
            self.index += 1
            #Si el indice llega al último elemento, volverá a 0
            if self.index >= len(self.images):
                self.index = 0
            #Dibujamos la imagen en pantalla (La volteamos para que mire a la derecha con flip)        
            self.image = pygame.transform.flip(self.images[self.index], True, False)
            self.image.set_colorkey(BLACK)
            self.countFPS = 0
        self.rect.x += x_speed
        self.rect.y += y_speed

#Cargamos el fondo de la escena
background = pygame.image.load("Pygame/images/background.png").convert()

#Iniciamos las variables globales que marcarán el movimiento del personaje
x_speed = 0
y_speed = 0

#Creamos el listado de los sprites, creamos al jugador y lo añadimos al listado de todos los sprites
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
    #Dibujamos el background
    screen.blit(background, [0, 0])
    #Dibujamos los sprites que tenemos en el grupo all_sprite_list
    all_sprite_list.draw(screen)
    #Ejecutamos el metodo update de los sprites que controlará el movimiento y las animaciones
    player.update()

    #Actualizamos pantalla
    pygame.display.flip()
    #Definimos los FPS que se mueve
    clock.tick(60)