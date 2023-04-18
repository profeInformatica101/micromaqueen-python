# Imports go at the top
from microbit import *
from maqueen import *


def moverComoPeon():
    robot.mover_celda()
    
def moverComoCaballo():
    robot.mover_celda()
    robot.mover_celda()
    robot.mover_celda()
    robot.girar_derecha()
    robot.mover_celda()

def moverComoTorre():
    for i in range(1,8):
     robot.mover_celda()

robot = Maqueen()

while True:
    if button_a.is_pressed():
        display.show("C")
        moverComoCaballo()
        
    elif button_b.is_pressed():
        display.show("P")
        moverComoPeon()
        
    else:
        display.show(Image.HEART)
