import microbit
import machine
import utime
import neopixel
import math

class Maqueen:
	"""
	Python class for DFRobot Micro:maqueen platform
	https://www.dfrobot.com/product-1783.html
	Author: Krzysztof Sawicki <krzysztof@rssi.pl>
	License: GNU
	"""

	def __init__(self):
		self.rgbleds = neopixel.NeoPixel(microbit.pin15, 4)
		print("MAQUEEN initialized")

	def set_led(self, lednumber, value):
		"""
		Enable or disable the front LEDS
		0 - left LED (P8)
		1 - right LED (P12)
		"""
		if lednumber == 0:
			microbit.pin8.write_digital(value)
		elif lednumber == 1:
			microbit.pin12.write_digital(value)

	def read_distance(self):
		"""
		Reads distance from HC SR04 sensor
		The result is in centimeters
		Divider is taken from Makecode library for micro:maqueen
		"""
		divider = 42
		maxtime = 250 * divider
		microbit.pin2.read_digital()  # just for setting PULL_DOWN on pin2
		microbit.pin1.write_digital(0)
		utime.sleep_us(2)
		microbit.pin1.write_digital(1)
		utime.sleep_us(10)
		microbit.pin1.write_digital(0)

		duration = machine.time_pulse_us(microbit.pin2, 1, maxtime)
		distance = duration/divider
		return distance

	def read_patrol(self, which):
		"""
		Reads patrol sensor
		"""
		if which == 0:  # left
			return microbit.pin13.read_digital()
		elif which == 1:  # right
			return microbit.pin14.read_digital()

	def set_motor(self, motor, value):
		"""
		Controls motor
		motor: 0 - left motor, 1 - right motor
		value: -255 to +255, the sign means direction
		"""
		data = bytearray(3)
		if motor == 0:  # left motor
			data[0] = 0
		else:
			data[0] = 2  # right motor is 2
		if value < 0:  # ccw direction
			data[1] = 1
			value = -1*value
		data[2] = value
		microbit.i2c.write(0x10, data, False)  # 0x10 is i2c address of motor driver

	def motor_stop_all(self):
		self.set_motor(0, 0)
		self.set_motor(1, 0)
    
	def turn_right(self):
		self.set_motor(0, 255)  # Motor izquierdo hacia adelante
		self.set_motor(1, -255)  # Motor derecho hacia atrás

	def turn_left(self):
		self.set_motor(0, -255)  # Motor izquierdo hacia atrás
		self.set_motor(1, 255)  # Motor derecho hacia adelante

	def stop(self):
		self.motor_stop_all()

	def forward(self):
		self.set_motor(0, 255)  # Motor izquierdo hacia adelante
		self.set_motor(1, 255)  # Motor derecho hacia adelante

	def mover_celda(self):
		"""
        Esta función permite al robot Maqueen moverse desde el centro de una celda hasta el centro de la siguiente celda.
        En un tablero de celdas de 9.5 cm de lado y con ruedas de 2 cm de radio, el robot avanzará de forma precisa
        para completar el movimiento entre las celdas.

        Uso:
        robot = Maqueen()
        robot.mover_celda()
        """
		radio_rueda = 2  # en centímetros
		distancia_celda = 9.5
		velocidad_ruedas = 1  # vueltas por segundo, ajustar según sea necesario
		circunferencia_rueda = 2 * math.pi * radio_rueda
		distancia_recorrer = distancia_celda + (distancia_celda / 2)
		num_vueltas_rueda = distancia_recorrer / circunferencia_rueda
		tiempo_mover = num_vueltas_rueda / velocidad_ruedas

		self.forward()
		utime.sleep(tiempo_mover)  # Ajustar este valor según sea necesario
		self.stop()
    
