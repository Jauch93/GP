from LEDArray import *
from DHT11 import *
from Ventilation import *
from Watering import *
from Grow import *
from gui import *
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
		GPIO.cleanup()

	def startGrow(self):
		self.activeGrow = Grow()

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
