import turtle

#Creamos la pantalla donde se renderizaran las cosas
screen = turtle.Screen
#dibujamos en la pantalla una flecha
tortuga = turtle.Turtle()

#Movemos por la pantalla la flecha, primero 100 pixeles hacia atras, luego la giramos 90 grados a la derecha, la movemos 100 pixeles hacia 
# adelante, la giramos 90 grados a la izquierda y la movemos hacia adelante 100 pixeles mas
tortuga.backward(100)
tortuga.right(90)
tortuga.forward(100)
tortuga.left(90)
tortuga.forward(100)

#Movemos la flecha a la coordenada especificada
tortuga.goto(100,100)

#dejamos la pantalla fija
turtle.done()