from microbit import *
import radio
from Maqueen import Maqueen

mq = Maqueen()

radio.on()
radio.config(channel=12, group=0)

while True:
    message = radio.receive()
    if message == 'left':
        mq.turn_left()
        sleep(500)  # Ajusta el tiempo de giro si es necesario
        mq.stop()
    elif message == 'right':
        mq.turn_right()
        sleep(500)  # Ajusta el tiempo de giro si es necesario
        mq.stop()
    elif message == 'forward':
        mq.forward()
        sleep(500)  # Ajusta el tiempo de avance si es necesario
        mq.stop()
    sleep(100)
