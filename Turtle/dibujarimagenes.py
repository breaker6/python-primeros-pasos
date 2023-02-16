import turtle
from turtle import Turtle, Screen

screen = turtle.Screen
screen2 = Screen()
screen2.screensize(800, 800)
screen2.register_shape("tifa-sprite.gif")
#tortuga = Turtle("tifa-sprite.gif")

mainCharacter = "tifa-sprite.gif"

#tortuga.addshape(name="tifa-sprite.gif", shape=None)
tortuga.shape("tifa-sprite.gif")


turtle.done()