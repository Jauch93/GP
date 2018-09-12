from LEDArray import *
from DHT11 import *

class GrowBox:
	def __init__(self):
		self.TF_Sensor = DHT11(7)
		self.Licht = LEDArray(18,12,11)

	def startGrow(self):
		self.activeGrow = Grow()
