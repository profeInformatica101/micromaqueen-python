# Imports go at the top
from microbit import *
from maqueen import *

maqueen_robot = Maqueen()
display.scroll(':)')

while True:
    display.show(Image.HEART)
    sleep(1000)
   
    maqueen_robot.forward()
    utime.sleep(2)

    maqueen_robot.turn_right()
    utime.sleep(1)

    maqueen_robot.turn_left()
    utime.sleep(1)

    maqueen_robot.stop()
