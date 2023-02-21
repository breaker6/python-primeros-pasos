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

score = 0

#Creamos la clase del item que recogeremos
class itemcollectible(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pygame/images/items/item-potion-green.png").convert()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        #Al iniciar el objeto, lo creamos en una posición aleatoria
        self.rect.x = random.randrange(800)
        self.rect.y = random.randrange(150, 500)

#Creamos la clase del sprite del personaje
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Pygame/images/tifa/battle_position/tifa-sprite-0000.png").convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        #Marcamos las coordenadas iniciales y lo dibujamos en ellas
        coord_x = 10
        coord_y = 150
        self.rect.x = coord_x
        self.rect.y = coord_y
    #Cuando se ejecuta el update, revisará si tiene que mover el objeto o no
    #Para ello, usamos las variables globales x_speed y y_speed
    def update(self):
        self.rect.x += x_speed
        self.rect.y += y_speed

#Definimos el tamaño de la ventana en la variable size y creamos la ventana
size = (800, 500)
screen = pygame.display.set_mode(size)
#Clock nos permitirá controlar los FPS del juego
clock = pygame.time.Clock()

#Ponemos la visibilidad del ratón en 0 para que no se vea
pygame.mouse.set_visible(0)

#Iniciamos las variables globales que marcarán el movimiento del personaje
x_speed = 0
y_speed = 0

#Cargamos la imagen de fondo
background = pygame.image.load("Pygame/images/background.png").convert()

#Creamos dos grupos de sprites que nos facilitará dibujarlos en pantalla
item_list = pygame.sprite.Group()
all_sprite_list = pygame.sprite.Group()

#Creamos 10 objetos coleccionables y los colocamos en posiciones aleatorias
for i in range(10):
    item = itemcollectible()
    #Añadimos los items que hemos creado a los grupos creados antes
    item_list.add(item)
    all_sprite_list.add(item)

#Creamos el objeto personaje y lo añadimos al grupo de todos los sprites
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
    screen.blit(background, [0, 0])
    #Dibujamos los sprites que tenemos en el grupo all_sprite_list
    all_sprite_list.draw(screen)
    #Ejecutamos el metodo update de los sprites. Esto hará que el personaje se mueva en función de si estamos pulsando
    all_sprite_list.update()

    #Creamos la lista de colisión. El primer parámetro y el segundo son los elementos de los que se detectarán las colisiones
    #El tercer parámetro será el que delimitará si el segundo objeto desaparece al colisionar. Estando en True, desaparece el segundo objeto
    item_hit_list = pygame.sprite.spritecollide(player, item_list, True)

    #Actualizamos la puntuación en consola
    for item in item_hit_list:
        score += 1
        print(score)

    #######Fin Zona de dibujo
    #Actualizamos pantalla
    pygame.display.flip()
    #Definimos los FPS que se mueve
    clock.tick(80)