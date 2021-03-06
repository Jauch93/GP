from LEDArray import *
from DHT11 import *
from Ventilation import *
from Watering import *
from Grow import *
from gui_MainWindow import *
import time
import RPi.GPIO as GPIO

class GrowBox:
	def __init__(self):
		self.tf_Sensor = DHT11(7)
		self.light = LEDArray(11)
		self.venti = Ventilation(15, self.tf_Sensor)
		self.water = Watering(13)
		self.startGrow()
		self.gui = MainWindow(self)

	def __del__(self):
		del self.tf_Sensor
		del self.light
		del self.venti
		del self.water
		GPIO.cleanup()
		print("GPIOs clean")

	def startGrow(self):
		self.activeGrow = Grow()

	def getDHT11(self):
		return self.tf_sensor

	def getLight(self):
		return self.light

	def getDHT11(self):
		return self.tf_Sensor

	def getVentilation(self):
		return self.venti

	def getWater(self):
		return self.water

	def getGrow(self):
		return self.activeGrow

	def turnAllOff(self):
		self.turnAllAutoOff()
		self.light.turnOff()
		self.water.turnOff()
		self.venti.turnOff()

	def turnAllOn(self):
		self.turnAllAutoOff()
		self.light.turnOn()
		self.water.turnOn()
		self.venti.turnOn()

	def turnAllAutoOff(self):
		self.light.stopAuto()
		self.water.stopAuto()
		self.venti.stopAuto()

	def turnAllAutoOn(self):
		self.light.startAuto()
		self.water.startAuto()
		self.venti.startAuto()
