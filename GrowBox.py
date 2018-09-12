from LEDArray import *
from DHT11 import *
from Ventilation import *
from Watering import *
from Grow import *
from gui import *

class GrowBox:
	def __init__(self):
		self.tf_Sensor = DHT11(7)
		self.licht = LEDArray(11)
		self.venti = Ventilation(15, self.tf_Sensor)
		self.water = Watering(13)
		self.startGrow()
		self.gui = gui(self)

	def startGrow(self):
		self.activeGrow = Grow()

	def getLight(self):
		return self.Licht

	def getDHT11(self):
		return self.tf_Sensor

	def getVenti(self):
		return self.venti

	def getWatering(self):
		return self.water

	def getGrow(self):
		return self.activeGrow
